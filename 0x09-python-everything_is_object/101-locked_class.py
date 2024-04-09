#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            # If the attribute already exists, allow assignment
            super().__setattr__(name, value)
        elif name == 'first_name':
            # Allow assignment only if the attribute is 'first_name'
            super().__setattr__(name, value)
        else:
            # Raise AttributeError for any other attribute assignment attempt
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
