from functools import partial
import numpy as _np

from simframe.frame.abstractgroup import AbstractGroup
from simframe.frame.field import Field
from simframe.frame.intvar import IntVar
from simframe.frame.heartbeat import Heartbeat
from simframe.utils.color import colorize
from simframe.utils.format import byteformat


class Group(AbstractGroup):
    """Class for grouping data. ``Group`` is a data frame that has additional functionality for updating its attributes.

    Notes
    -----
    When ``Group.update()`` is called the instructions of the group's ``Heartbeat`` object will be performed.
    The function that is determing the update operation needs the parent ``Frame`` object as first positional argument."""

    __name__ = "Group"

    def __init__(self, owner, updater=None, description=""):
        """Parameters
        ----------
        owner : Frame
            Parent frame object to which the group belongs
        updater : Heartbeat, Updater, callable, list or None, optional, default : None
            Updater for group update. A Heartbeat object will be created from this.
        description : string, optional, default : ""
            Descriptive string for the group

        Notes
        -----
        The updater of groups can take a list of string with the attribute names that should be updated
        in the order in which they should be updated. It will create a callable function from that list."""
        self._description = description
        self._owner = owner
        self._updateorder = None
        self.updater = updater

    def __setattr__(self, name, value):
        """Function to set an attribute including fields.
        This function allows the user to change the value of fields instead of replacing them."""
        if name in self.__dict__ and isinstance(self.__dict__[name], Field):
            self.__dict__[name]._setvalue(value)
        else:
            super().__setattr__(name, value)

    def __repr__(self):
        """Function to have good looking overview of the members of the group."""

        fields = {}
        groups = {}
        misc = {}

        # return value
        ret = ""

        for key, val in self.__dict__.items():
            # Don't show private attributes
            if key.startswith("_"):
                continue

            # Sort attributes by group, field and else
            if isinstance(val, Field):
                fields[key] = val
            elif isinstance(val, Group):
                groups[key] = val
            else:
                misc[key] = val

        # Underlined headline. The length of the underline is off if there are hidden characters, like color.
        ret += self.__str__() + "\n"
        ret += "-" * (len(ret) - 1) + "\n"

        # Printing all groups alphanumerically sorted by name
        if len(groups) > 0:
            for key in sorted(groups.keys(), key=str.casefold):
                if len(key) > 12:
                    name = key[:9] + "..."
                else:
                    name = key
                ret += "    {:12s} : {}\n".format(name, groups[key])
            ret += "  -----\n"

        # Printing all fields alphanumerically sorted by name
        if len(fields) > 0:
            for key in sorted(fields.keys(), key=str.casefold):
                if len(key) > 12:
                    name = key[:9] + "..."
                else:
                    name = key
                ret += "    {:12s} : {}\n".format(name, fields[key].__str__())
            ret += "  -----\n"

        # Printing everything else alphanumerically sorted
        if len(misc) > 0:
            for key in sorted(misc.keys(), key=str.casefold):
                if len(key) > 12:
                    name = key[:9] + "..."
                else:
                    name = key
                ret += "    {:12s} : {}\n".format(name,
                                                  type(misc[key]).__name__)
            ret += "  -----\n"

        # The Frame object should have an integrator and writer which are displayed separately.
        # If the object has an integrator
        if "_integrator" in self.__dict__.keys():
            integrator = self.__dict__["_integrator"]
            # If not set, print warning
            txt = colorize("not specified", "yellow")
            if integrator is not None:
                txt = integrator.__str__()
            ret += "    {:12s} : {}".format("Integrator", txt)
            ret += "\n"

        # If the object has a writer
        if "_writer" in self.__dict__.keys():
            writer = self.__dict__["_writer"]
            # If not set print warning
            txt = colorize("not specified", "yellow")
            if writer is not None:
                txt = writer.__str__()
            ret += "    {:12s} : {}".format("Writer", txt)
            ret += "\n"

        return ret

    @property
    def updateorder(self):
        '''Update order if updater was set with list of strings. ``None`` otherwise.'''
        return self._updateorder

    @updateorder.setter
    def updateorder(self, value):
        raise RuntimeError("Do not set this attribute manually.")

    # We need to overwrite the updater property of AbstractGroup, because we want the group to be able
    # to take lists of attributes as value.
    @property
    def updater(self):
        '''``Heartbeat`` object with update instructions.

        You can either set a ``Heartbeat`` object directly, a callable functions that will be automatically transformed into
        a ``Heartbeat`` object, or a list of attribute names of the ``Group`` that will be updated in that order.'''
        return self._updater

    @updater.setter
    def updater(self, value):
        if isinstance(value, Heartbeat):
            self._updater = value
            self._updateorder = None
        elif isinstance(value, list):
            self._checkupdatelist(value)
            self._updater = Heartbeat(self._createupdatefromlist(value))
            self._updateorder = value.copy()
        else:
            self._updater = Heartbeat(value)
            self._updateorder = None

    @property
    def toc(self):
        '''Complete table of contents starting from this object.'''
        self._toc()

    @toc.setter
    def toc(self, value):
        pass

    def addfield(self, name, value, updater=None, differentiator=None, description="", constant=False, save=True, copy=True):
        """Function to add a new ``Field`` to the object.

        Parameters
        ----------
        name : string
            Name of the field
        value : number, array, string
            Initial value of the field. Needs to have already the correct type and shape
        updater : Heartbeat, Updater, callable or None, optional, default : None
            Updater for field update
        differentiator : Heartbeat, Updater, callable or None, optional, default : None
            Differentiator if the field has a derivative
        description : string, optional, default : ""
            Descriptive string for the field
        constant : boolean, optional, default : False
            True if the field is immutable
        save : boolean, optional, default : True
            If True field will be stored in output files
        copy : boolean, optional, default : True
            If True <value> will be copied, not referenced
        """
        self.__dict__[name] = Field(self._owner, value, updater=updater,
                                    differentiator=differentiator, description=description, constant=constant, save=save, copy=copy)

    def addgroup(self, name, updater=None, description=""):
        """Function to add a new ``Group`` to the object.

        Parameters
        ----------
        name : string
            Name of the group
        updater : Heartbeat, Updater, callable or None, optional, default : None
            Updater for field update
        description : string, optional, default : ""
            Descriptive string for the group
        """
        self.__dict__[name] = Group(
            self._owner, updater=updater, description=description)

    def addintegrationvariable(self, name, value, snapshots=[], updater=None, description="", copy=True):
        """Function to add a new integration variable ``IntVar`` to the object.

        Parameters
        ----------
        name : string
            Name of the field
        value : number, array, string
            Initial value of the field. Needs to have already the correct type and shape
        updater : Heartbeat, Updater, callable or None, optional, default : None
            Updater for field update
        snapshots : list, ndarray, optional, default : []
            List of snapshots at which an output file should be written
        description : string, optional, default : ""
            Descriptive string for the field
        copy : boolean, optional, default : True
            If True <value> will be copied, not referenced
        """
        self.__dict__[name] = IntVar(
            self._owner, value, updater=updater, snapshots=snapshots, description=description, copy=copy)

    def _checkupdatelist(self, ls):
        """This function checks if a list is suitable to be used as update.

        Parameters
        ----------
        ls : list
            list of string with the attribute names that should be updated in that order"""
        for val in ls:
            if not isinstance(val, str):
                raise ValueError("List has to be list of strings.")
        for val in ls:
            if val not in self.__dict__:
                raise RuntimeError(
                    "{} is not an attribute of the group".format(val))

    def _createupdatefromlist(self, ls):
        """This method creates an update method from a list.

        Parameters
        ----------
        ls : list
            list of group attributes that should be updated in that order

        Returns
        -------
        func : callable
            Function that is reduced by <self> and <ls>."""

        # To give meaningful information a new class of partial is created
        # with a new __repr__ method
        class list_updater(partial):

            def __repr__(self):
                return type(self).__name__

        f = list_updater(_dummyupdatewithlist, self, ls)
        f.__doc__ = f"The attributes in this group are updated in the order: \n{ls}."
        return f

    def _toc(self):
        ret = _toc_tree(self)
        print(ret)

    def memory_usage(self, print_output=False, skip_hidden=False):
        """Determine memory usage of a Group

        Will only return the correct data size of Fields and Groups of Fields.
        Other data types might deviate from the true memory usage.

        Parameters
        ----------
        print_output : bool, optional, default : False
            if True, print results on screen
        skip_hidden : bool, optional, default : False
            if True, hidden attributes will be ignored

        Returns
        -------
        float
            total memory usage of group in bytes
        """
        res, total = _mem_tree(self, skip_hidden=skip_hidden)
        if print_output:
            print(res)
            print("Total: "+byteformat(total))
        return total


def _mem_tree(obj, prefix="", skip_hidden=True):
    ret = ""
    total = 0.0
    prefix = prefix + 4 * " "
    for key in sorted(obj.__dict__.keys(), key=str.casefold):
        if key == "_owner":
            continue
        if skip_hidden & key.startswith("_"):
            continue
        val = obj.__dict__[key]
        part1 = "{}- {}: ".format(prefix, colorize(key, "blue"))
        if isinstance(val, Group):
            part2, size = _mem_tree(val, prefix=prefix)
            ret += part1.ljust(56) + \
                "total: " + byteformat(size) + "\n" + part2
        else:
            if isinstance(val, _np.ndarray):
                size = val.nbytes
                shape = str(val.shape).rjust(17)
            else:
                size = val.__sizeof__()
                shape = " " * 17
            s = byteformat(size)
            part2 = shape + " " + s
            ret += (part1).ljust(45) + part2 + "\n"

        s = byteformat(size)
        total += size
    return ret, total


def _toc_tree(obj, prefix=""):
    ret = colorize(obj.__str__(), "blue")
    prefix = prefix + 4 * " "
    for key in sorted(obj.__dict__.keys(), key=str.casefold):
        if key.startswith("_"):
            continue
        val = obj.__dict__[key]
        ret += "\n{}- {}: ".format(
            prefix, colorize(key, "blue"))
        if isinstance(val, Group):
            ret += _toc_tree(val, prefix=prefix)
        else:
            ret += val.__str__()
    return ret


def _dummyupdatewithlist(grp, ls, owner, *args, **kwargs):
    """This method is a dummy method that updates all attributes given in ls.

    Parameters
    ----------
    grp : Group
        group to which the attributes belong
    ls : list
        List of string with attributes of group that should be updated in that order
    owner : Frame
        Parent frame object
    args : additional positional arguments
    kwargs : additional keyword arguments

    Notes
    -----
    args and kwargs are only passed to the updater of the Heartbeat, NOT systole or diastole."""
    for val in ls:
        grp.__dict__[val].update(*args, **kwargs)
