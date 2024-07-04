# Developed by Jayme Hebinck, for bachelor thesis Leiden University.
# This file is part of the ADT Create project, found on: https://github.com/MainJay/ADTPythonLibrary/

from . import ADT

class GenADTerms:
    """
    Contains functions regarding ADTerms Generation operations on `ADT` objects.
    """
    def __init__(self, ADT: 'ADT.ADT') -> None:
        """
        Links `GenADTerms` object to `ADT` object. `GenADTerms` object is initialized when `ADT` object is initialized.
        :param ADT: Links `ADT` object to this `GenADTerms` object, to make sure these two objects are linked correctly.
        """
        self.ADT = ADT

    def ADTermsIntermediary(self, result: str) -> str:
        """
        Determines ADTerm of an intermediary node (no counter child node) in the ADT.

        :param result: Current ADTerm of children nodes.
        :return:`str`: DTerm of intermediary node.

        Note: *Helper function, users should not call this function themselves. Used in member function: `determineADTerms(...)`.*
        """
        newRes = ""  # Empty string
        # Add refinement and type to string. Proponent will be the type of the root node, Opponent the counternode.
        if self.ADT.type == self.ADT.root[1].type:
            if self.ADT.refinement == 0:
                newRes += '∨p['
            else:
                newRes += '∧p['
        else:
            if self.ADT.refinement == 0:
                newRes += '∨o['
            else:
                newRes += '∧o['
        # Add children labels between brackets.
        newRes += f'{result}]'
        return newRes

    def ADTermsIntermediaryWithCounter(self, counterChild: 'ADT.ADT') -> str:
        """
        Determines ADTerm of an intermediary node with counter child node in the ADT.

        :param counterChild: ADTerm of counter child node.
        :return: `str`: ADTerm of intermediary node.

        Note: *Helper function, users should not call this function themselves. Used in member function: `determineADTerms(...)`.*
        """
        # Reasoning why the current result is NOT being used in this function:
        # Result is already a string with all subresults combined up until this point.
        # The problem is, in this function (only this one) this subresult must be altered, and is not just concatenated
        # to other parts of the string. Therefore, the choice was made to remake this subresult using the saved ADTerms
        # in the nodes of the ADT.
        # This is the most effective way for this function, and using the subresult is the most effective way for
        # other functions. Therefore, this choice has been made.

        newRes = ""  # Empty string
        # Add counter symbol, refinement and type to string
        if self.ADT.type == self.ADT.root[1].type:
            newRes += 'cp['
            if self.ADT.refinement == 0:
                newRes += '∨p['
            else:
                newRes += '∧p['
        else:
            newRes += 'co['
            if self.ADT.refinement == 0:
                newRes += '∨o['
            else:
                newRes += '∧o['

        combinedADTerms = ""  # New empty string to determine belonging children and counter children.
        for thisChild in self.ADT.children:
            if thisChild is not counterChild:
                # For every child, check if this child is not the defense child.
                if combinedADTerms == "":
                    # If first belonging child, do not add any commas.
                    combinedADTerms += thisChild.ADTerms
                else:
                    # If other belong child, add child using a comma before.
                    combinedADTerms += ", " + thisChild.ADTerms
        # Firstly add all belonging children and close this section using ']', then add counter child and close this
        # section using ']' as well.
        combinedADTerms += "], " + counterChild.ADTerms + "]"
        newRes += combinedADTerms  # Concatenate the children to the determined symbols and return.
        return newRes


    def ADTermsSingleNodeWithCounter(self, result: str) -> str:
        """
        Determines ADTerm of an intermediary node (no counter child node) in the ADT.

        :param result: Current ADTerm of children nodes.
        :return: `str`: ADTerm of intermediary node.

        Note: *Helper function, users should not call this function themselves. Used in member function: `determineADTerms(...)`.*
        """
        newRes = ""  # Emptry string
        # Add counter symbol, refinement is not needed.
        if self.ADT.type == self.ADT.root[1].type:
            newRes += 'cp['
        else:
            newRes += 'co['
        # Add first the parent label, then the child label to the ADTerms string.
        newRes += f'"{self.ADT.label}"'
        newRes += f', {result}]'
        return newRes


    def determineADTerms(self) -> str:
        """
        Determines ADTerm of the ADT, with the node it is run on as the root node.

        :return: `str`: ADTerm of the ADT in string format.

        Note: *This function is called from the `ADT` class using `determineADTerms(...)`, and should therefore not be called from the `GenADTerms` class.*
        """
        # Create empty string
        result = ""
        for i in range(len(self.ADT.children)):
            # Save subRes determined from children
            subRes = self.ADT.children[i].determineADTerms()
            if i == 0:
                # If first element, then no comma in between. Otherwise, comma in between.
                result += f'{subRes}'
            else:
                result += f', {subRes}'
        if self.ADT.leafNode:
            # if self.type == self.parent.type:
            result += f'"{self.ADT.label}"'  # Get ADTerms of a leaf node.
        else:
            # If this node is not a leaf node:
            if len(self.ADT.children) == 1:
                # If this node has only one child.
                if self.ADT.children[0].type == self.ADT.type:
                    # Add brackets in between the child to show it is a level deeper (if child is of same type).
                    result = "[" + result + "]"
                else:
                    # Otherwise there is one child with the opposite type, get ADTerms.
                    result = self.ADTermsSingleNodeWithCounter(result)
            else:
                for child in self.ADT.children:
                    # Otherwise, if there are > 1 children, then check for type.
                    if child.type is not self.ADT.type:
                        # If one child of opposite type, get ADTerms.
                        result = self.ADTermsIntermediaryWithCounter(child)
                        break
                else:
                    # Otherwise, if there are > 1 children of the same type, get ADTerms.
                    result = self.ADTermsIntermediary(result)
        self.ADT.ADTerms = result  # Save current ADTerms in the current node.
        return result
