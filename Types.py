# Author : Sasidhar@gmail.com
# Project demo library for Odata consumption and creation in python
# EDM CSDL 2.3


class Documentation(object):
    pass


# EDM CSDL 2.3
# EDM Documentation element , can have only only summary and only one long description
# A model element MUST NOT contain more than one documentation element.

class Documentation_Impl(Documentation):
    def __init__(self):
        self._summary = None
        self._long_description = None
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @summary.deleter
    def summary(self):
        del self._summary

    @property
    def long_description(self):
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        self._long_description = value

    @long_description.deleter
    def long_description(self):
        del self._long_description

    def is_summary_avl(self):
        if not self._summary is None:
            return True
        else:
            return False

    def is_long_description_avl(self):
        if not self._long_description is None:
            return True
        else:
            return False

