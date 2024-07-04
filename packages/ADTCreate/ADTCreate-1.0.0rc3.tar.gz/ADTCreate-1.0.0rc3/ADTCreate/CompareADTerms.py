# Developed by Jayme Hebinck, for bachelor thesis Leiden University.
# This file is part of the ADT Create project, found on: https://github.com/MainJay/ADTPythonLibrary/.

from ADTCreate.MultisetList import MSList
import math
import Levenshtein
import numpy as np

from . import ADT
from . import MultisetList
from typing import List, Tuple, Dict, Union, Optional

class CompADTerms:
    """
    Contains functions regarding ADTerms Comparison operations on `ADT` objects.
    """
    def __init__(self, ADT: 'ADT.ADT') -> None:
        """
        Links `CompADTerms` object to `ADT` object. `CompADTerms` object is initialized when `ADT` object is initialized.
        :param ADT: Links `ADT` object to this `CompADTerms` object, to make sure these two objects are linked correctly.
        """
        self.ADT = ADT

    def generateItemsToCompare(self, ADTermsMS: str) -> 'MultisetList.MSList':
        """
        Generates items to compare based on ADTerms string and put the items in a multiset.

        :param ADTermsMS: ADTerm that should have its items converted into a multiset.
        :return: `MSList` object: multiset list object with all items of ADTerm string.

        Note: *Helper function, users should not call this function themselves. Used in member function: `multisetEquivalenceCheck(...)`.*
        """
        depthLevel = 0  # Depth level is kept to only generate items that are on the surface level.
        inString = False  # Keep track of whether we are working on a string right now.
        itemsToCompare = MSList()  # Keep track of all separate items.
        entry = ""  # Initialize empty entry in itemsToCompare MSList.
        for charIndex in range(len(ADTermsMS)):
            if ADTermsMS[charIndex] == "[" and not inString:
                # If this character is a [ and we are not working on a string, go a level deeper.
                depthLevel += 1
            elif ADTermsMS[charIndex] == "]" and not inString:
                # If this character is a ] and we are not working on a string, go a level undeeper.
                depthLevel -= 1
            elif ADTermsMS[charIndex] == "\"" and depthLevel == 0:
                # If this character is a " and we are on the surface level.
                if not inString:
                    # If a string has not been opened yet, open a string and add this character to the entry.
                    inString = True
                    entry += ADTermsMS[charIndex]
                elif (inString) and (charIndex + 1 < len(ADTermsMS) - 1) and not (
                        ADTermsMS[charIndex + 1] == "," or ADTermsMS[charIndex + 1] == "]"):
                    # If a string has been opened, and this is a " with no , or ] after it, then this " is part of the string.
                    entry += ADTermsMS[charIndex]  # Add this character to the entry.
                elif inString:
                    # If this is a string and the next character is a , or ], this is the end of the string.
                    inString = False
                    entry += ADTermsMS[charIndex]  # Add this character to the entry.
                    itemsToCompare.append(entry)  # Add entry to the itemsToCompare MSList.
                    entry = ""  # Initialize new empty entry.
            elif inString and depthLevel == 0:
                # If we are working on a string and we are on the surface level, add this character to the entry.
                entry += ADTermsMS[charIndex]
            elif (ADTermsMS[charIndex] == "∧" or ADTermsMS[charIndex] == "∨" or ADTermsMS[
                charIndex] == "c") and depthLevel == 0:
                # If the current character is a symbol and we are on the surface level, add it to the entry.
                if ADTermsMS[charIndex] == "c" and ADTermsMS[charIndex + 2] == "[" and (
                        ADTermsMS[charIndex + 3] == "∧" or ADTermsMS[charIndex + 3] == "∨"):
                    # If this symbol is a counter symbol, check if a ∧ or a ∨ symbol follows directly. If so, add these
                    # symbols to the entry.
                    entry += ADTermsMS[charIndex]
                    entry += ADTermsMS[charIndex + 1]
                    entry += ADTermsMS[charIndex + 2]
                    entry += ADTermsMS[charIndex + 3]
                    entry += ADTermsMS[charIndex + 4]
                else:
                    # If this symbol is not a counter symbol, or this counter symbol does not have any direct other
                    # symbols, add only the counter symbol to the entry.
                    entry += ADTermsMS[charIndex]
                    entry += ADTermsMS[charIndex + 1]
                itemsToCompare.append(entry)  # Add entry to the itemsToCompare MSList.
                entry = ""  # Initialize new empty entry.
        return itemsToCompare


    def determineLevenshteinDistance(self, labelMS1: str, MS2: MultisetList.MSList) -> Tuple[bool, Optional[str], Optional[int]]:
        """
        Determines the Levenshtein Distance between a label from the label we want to compare to all elements in the other multiset. Determines if label is within equivalence threshold of any other label from the other multiset, and picks the label that has the shortest Levenshtein Distance and is within the equivalence threshold.

        :param labelMS1: String with label that needs to be compared.
        :param MS2: Multiset with all elements from other ADTerm.
        :return: `bool`, `string`/`None`, `int`/`None`: `True`, element with smallest Levenshtein Distance, Levenshtein Distance if label has been found within equivalence threshold, `False`, `None`, `None` otherwise.

        Note: *Helper function, users should not call this function themselves. Used in member functions: `multisetEquivalenceCheck(...)`, `parentChildCheck(...)`.*
        """
        possibleEntry = []
        for element in MS2:
            # For every element in MS2
            if element[0] == "\"" and element[-1] == "\"":
                longestLabel = max(len(labelMS1) - 2,
                                   len(element) - 2)  # Takes length of biggest label (both -2 to remove the " before and after the label).
                errorAcceptThreshold = math.ceil(longestLabel * self.ADT.LSEquivalenceThreshold)
                # If this element starts and ends with ", we know it is a label.
                if Levenshtein.distance(labelMS1, element) <= errorAcceptThreshold:
                    entry = [element, Levenshtein.distance(labelMS1, element)]
                    possibleEntry.append(entry)
                    # Perform Levenshtein Distance, if within error threshold, return true, the element of MS2 and Levenshtein Distance.
        if not possibleEntry:
            return False, None, None
        smallest = np.Inf
        smallestEntry = None
        for entry in possibleEntry:
            if entry[1] < smallest:
                smallestEntry = entry
                smallest = entry[1]
        return True, smallestEntry[0], smallestEntry[1]
        # If no label found that is within error threshold, return False.



    def multisetEquivalenceCheck(self, ADTermsMS1: 'MultisetList.MSList', ADTermsMS2: 'MultisetList.MSList') -> Tuple[bool, int]:
        """
        Checks whether the two multisets containing elements of ADTerm on a specific level of abstraction, and checks if the these two multisets are equivalent.

        :param ADTermsMS1: ADTerm to compare with.
        :param ADTermsMS2: ADTerm to compare with.
        :return: `bool`, `int`/`None`: `True` and total Levenshtein Distance (`Int`) if equivalent, `False` and `None` otherwise.

        Note: *Helper function, users should not call this function themselves. Used in member functions: `recursiveComparison(...)`, `compareADTerms(...)`.*
        """
        MS1 = self.generateItemsToCompare(ADTermsMS1)  # Generate MS of items to compare of ADTerms1
        MS2 = self.generateItemsToCompare(ADTermsMS2)  # Generate MS of items to compare of ADTerms2
        totalLevenShteinDistance = 0
        for element in MS1:
            MS2Copy = MS2
            if element[0] == "\"" and element[-1] == "\"":
                # If this element in the Multiset is a label.
                resultLS = self.determineLevenshteinDistance(element, MS2Copy)
                if not resultLS[0]:
                    return False, 0
                totalLevenShteinDistance += resultLS[2]
                MS2[MS2.index(resultLS[1])] = element  # Change this entry temporarily in this MS so that the final check
                # will pass with the Levenshtein distance processed.
        if MS1 == MS2:
            # Compare ADTerms1 vs ADTerms2, if equivalent, return True with total Levenshtein Distance so far.
            return True, totalLevenShteinDistance
        # Else, return False
        return False, 0


    def selectCurrentMultisetStr(self, ADTerms: str) -> str:
        """
        Selects elements of ADTerm on a specific level of abstraction and saves them in string format.

        :param ADTerms: ADTerm to select elements of.
        :return: `str`: string of elements of ADTerm.

        Note: *Helper function, users should not call this function themselves. Used in member function: `recursiveComparison(...)`.*
        """
        depthLevel = 0  # Depth level is kept to only select the Multiset parts that are one level deeper.
        MSParts = MSList()  # Keep track of all separate parts of deeper Multisets
        inBetween = False  # Keep track of whether we are in between two separate deeper level Multisets.
        for charIndex in range(len(ADTerms)):
            if ADTerms[charIndex] == "[" and depthLevel == 0:
                # If this character is a [ and we are on the surface level, we determine that this is the start of a new
                # deeper level Multiset. Set inBetween on False, openPos to the next character and depthlevel a level
                # deeper.
                inBetween = False
                openPos = charIndex + 1
                depthLevel += 1
            elif ADTerms[charIndex] == "[" and depthLevel > 0:
                # If this character is a [ and we are already in a deeper level, we are not interested in this
                # Multiset yet. Set depthLevel a level deeper.
                depthLevel += 1
            elif ADTerms[charIndex] == "]" and depthLevel == 1:
                # If this character is a ] and the depthLevel is 1, this is the end of the deeper level Multiset.
                # Depthlevel will now be set back to surface level (0), closePos is set to this character,
                # MSParts saves this deeper Multiset, and we are now potentially inBetween two Multisets, so set
                # inBetween to True.
                depthLevel -= 1
                closePos = charIndex
                MSParts.append(ADTerms[openPos:closePos])
                inBetween = True
            elif ADTerms[charIndex] == "]" and depthLevel > 1:
                # If this character is a ] and depthLevel is higher than 1, we are not interested in this Multiset yet.
                # Set depthLevel a level undeeper.
                depthLevel -= 1
            elif (ADTerms[charIndex] == "," or ADTerms[charIndex] == " ") and depthLevel == 0 and inBetween:
                # If this character is a , or a ' ', and we are on the surface level and in between two Multisets,
                # add this , or ' ' to the MSParts.
                MSParts += ADTerms[charIndex]
            elif (ADTerms[charIndex] != "," or ADTerms[charIndex] != " ") and inBetween:
                # If this character is not a , or a ' ', and we are inBetween two Multisets, we can determine that there
                # will not be a next Multiset. Set inBetween to False.
                inBetween = False
        totalString = "".join(MSParts)  # After all MSParts are saved, join them together in a string.
        return totalString  # Return this deeper most outer Multiset as string.


    def splitMultiset(self, ADTerms: str) -> 'MultisetList.MSList':
        """
        Split given Multiset into different entries (entries are current level (intermediary/leaf) nodes).

        :param ADTerms: ADTerm to select elements of.
        :return: `MSList`: Multiset of elements of ADTerm.

        Note: *Helper function, users should not call this function themselves. Used in member function: `parentChildCheck(...)`.*
        """
        # Split given Multiset into different entries (entries are current level (intermediary/leaf) nodes)
        # Important to note: since spaces between entries are no longer of use, we strip the individual entries before adding
        # them to the entries MSList
        depthLevel = 0
        startPos = 0
        entries = MSList()
        for charIndex in range(len(ADTerms)):
            if ADTerms[charIndex] == "[":
                # When character [ is seen, we are a level deeper.
                depthLevel += 1
            if ADTerms[charIndex] == "]":
                # When character ] is seen, we are a level undeeper.
                depthLevel -= 1
            if ADTerms[charIndex] == "," and depthLevel == 0:
                # When a comma is seen, and we are on the surface level, we determine that this is a separation of an entry.
                endPos = charIndex
                entry = ADTerms[startPos:endPos].strip()
                entries.append(entry)
                startPos = charIndex + 1
        # Last part of the string is also an entry.
        entry = ADTerms[startPos:].strip()
        entries.append(entry)
        return entries


    def getSymbol(self, entryMS: str) -> str:
        """
        Separates symbol from multiset.

        :param entryMS: Multiset which contains multiset.
        :return: `str`: Symbol if there, otherwise `""`.

        Note: *Helper function, users should not call this function themselves. Used in member function: `parentChildCheck(...)`.*
        """
        # Get symbol of current level ADTerms entries. If no symbol (just a label name), return empty string instead.
        for charIndex in range(len(entryMS)):
            if entryMS[charIndex] == "[":
                symbol = entryMS[:charIndex]
                return symbol
        else:
            return ""


    def generateParentChildPairs(self, elementsADTerms: 'MultisetList.MSList', entriesMS: 'MultisetList.MSList') -> MultisetList.MSList:
        """
        Generate pairs of deeper level ADTerms entries and current level ADTerms symbols.

        :param elementsADTerms: Contains symbols of ADTerm.
        :param entriesMS: Contains labels of multiset.
        :return: `MSList`: multiset with pairs between labels and symbols.

        Note: *Helper function, users should not call this function themselves. Used in member function: `parentChildCheck(...)`.*
        """
        # Generate pairs of deeper level ADTerms entries and current level ADTerms symbols.
        pairs = MSList()
        for element in elementsADTerms:
            for entry in range(len(entriesMS)):
                if element in entriesMS[entry]:
                    # If deeper level part of ADTerms is found in current level ADTerms, save the symbol it must be
                    # connected to from current level ADTerms, and make a pair containing a list of all labels from the
                    # deeper level ADTerms and the current level ADTerms symbol that they have to be present under.
                    symbol = self.getSymbol(entriesMS[entry])
                    pair = (self.generateNodeLabels(element), symbol)
                    pairs.append(pair)  # Append this pair to MSList of pairs.
        # All pairs are added in the pairs MSList. Return this MSList.
        return pairs


    def generateNodeLabels(self, ADTerms: str) -> 'MultisetList.MSList':
        """
        Generate a multiset with the labels in this ADTerms.

        :param ADTerms: ADTerm string which contains the labels.
        :return: `MSList`: multiset with labels of the node.

        Note: *Helper function, users should not call this function themselves. Used in member function: `generateParentChildPairs(...)`.*
        """
        # Generate a MSList with the labels in this ADTerms.
        labels = MSList()
        label = ""
        inString = False
        for charIndex in range(len(ADTerms)):
            # A label is present between "".
            if ADTerms[charIndex] == "\"" and not inString:
                label += ADTerms[charIndex]
                inString = True
            elif ADTerms[charIndex] == "\"" and inString:
                label += ADTerms[charIndex]
                labels.append(label)
                label = ""
                inString = False
            elif inString:
                label += ADTerms[charIndex]
        # Return the MSList with all labels.
        return labels


    def parentChildCheck(self, ADTerms1: str, ADTerms2: str, oldADTerms1: str, oldADTerms2: str) -> bool:
        """
        Generate entries for Multisets of deeper level ADTerms and current level ADTerms. Generate pairs of deeper level ADTerms and current level ADTerms symbols. Parent-Child relationship is established. Compare pairs of multisets. If one pair is not found in the other pair, parent-child relationship is not maintained.

        :param ADTerms1: ADTerm of current level.
        :param ADTerms2: ADTerm of current level.
        :param oldADTerms1: ADTerm of deeper level.
        :param oldADTerms2: ADTerm of deeper level.
        :return: `bool`: `True` if parent-child relationships are equivalent, `False` otherwise.

        Note: *Helper function, users should not call this function themselves. Used in member functions: `recursiveComparison(...)`, `compareADTerms(...)`.*
        """
        # Generate entries for Multisets of deeper level ADTerms and current level ADTerms
        entriesMS1 = self.splitMultiset(ADTerms1)
        entriesMS2 = self.splitMultiset(ADTerms2)
        splitElementsADTerms1 = self.splitMultiset(oldADTerms1)
        splitElementsADTerms2 = self.splitMultiset(oldADTerms2)

        # Generate pairs of deeper level ADTerms and current level ADTerms symbols. Parent-Child relationship is established.
        pairsMS1 = self.generateParentChildPairs(splitElementsADTerms1, entriesMS1)
        pairsMS2 = self.generateParentChildPairs(splitElementsADTerms2, entriesMS2)

        # Compare pairs of multisets. If one pair is not found in the other pair, parent-child relationship is not maintained.
        # This means that these two ADTerms are not equivalent.
        # Important note: we are only comparison the labels present in the deeper level ADTerms, not the whole ADTerms
        # structure. Labels is enough considering the ADTerms structure is compared in deeper checks.
        # This check is only for parent-child relationship, where it is important that the labels are part of the
        # deeper level ADTerms that are connected to the right symbol of the current level ADTerms.
        labelsFound = False  # If all labels are found in a given entry of the other Multiset.
        for entryMS1 in pairsMS1:
            # For an entry in the pairs of Multiset 1.
            if entryMS1 not in pairsMS2:
                # If this entry is not exactly in the pairs of Multiset 2.
                for entryMS2 in pairsMS2:
                    # Check for every label in every entry of Multiset 2 if it is within error threshold of first label
                    # in the entry of Multiset 1.
                    resultLS = self.determineLevenshteinDistance(entryMS1[0][0], entryMS2[0])
                    if resultLS[1]:
                        # If the first label of the entry of Multiset 1 finds a label in the entry of Multiset 2 within
                        # error threshold, we test all other labels of Multiset 1 on this entry of Multiset 2.
                        labelsFound = True
                        for label in entryMS1[0]:
                            if label != entryMS1[0][0]:
                                # We skip the first label, since we already determined that one was found.
                                labelsResultLS = self.determineLevenshteinDistance(label, entryMS2[0])
                                if not labelsResultLS[1]:
                                    # If any of the other labels in the entry of Multiset 1 are not within the error
                                    # threshold of the labels in the entry of Multiset 2, these pairs are not equivalent.
                                    labelsFound = False
                                    break
                        if labelsFound:
                            # If all labels in the entry of Multiset 1 are within the error threshold of (or equal to)
                            # all the labels in the entry of Multiset 2, these pairs are equivalent.
                            break
                        # break
                if not labelsFound:
                    # If one or more of the labels in the entry of Multiset 1 are not within the error threshold of
                    # the labels in the entry of Multiset 2, these pairs are not equivalent.
                    return False
                labelsFound = False  # After this check, reset labelsFound boolean back to False for next check.
        # If no proof is found against equivalence, return True.
        return True


    def recursiveComparison(self, ADTerms1Sub: str, ADTerms2Sub: str, continueCheck: bool, equivalence: bool) -> Tuple[bool, str, str, int]:
        """
        Recursively compares two ADTerms by performing the top-down method and bottom-up method.

        :param ADTerms1Sub: String of part of ADTerm that needs to be compared.
        :param ADTerms2Sub: String of part of ADTerm that needs to be compared.
        :param continueCheck: Boolean that determines if we continue the check, or not when equivalence is disproved.
        :param equivalence: Boolean that shows if the ADTerm is equivalent or not (within equivalence threshold).
        :return: `bool`, `str`, `str`, `int`: `True`, string of part of ADTerm, string of part of ADTerm and Levenshtein Distance when equivalent till this point, `False`, string of part of ADTerm, string of part of ADTerm and `0` when no longer equivalent.

        Note: *Helper function, users should not call this function themselves. Used in member functions: `recursiveComparison(...)`, `compareADTerms(...)`.*
        """
        if continueCheck:
            # As long as we have not found a problem, continue checking.
            ADTerms1Selected = self.selectCurrentMultisetStr(ADTerms1Sub)  # Get deeper level ADTerms
            ADTerms2Selected = self.selectCurrentMultisetStr(ADTerms2Sub)  # Get deeper level ADTerms
            ADTerms1Sub, ADTerms2Sub = ADTerms1Selected, ADTerms2Selected  # Save current level ADTerms
            totalLevenshteinDistance = 0
            if ADTerms1Sub == "" and ADTerms2Sub == "":
                # If both ADTerms are empty, check has finished successfully. Return with equivalence == True.
                return equivalence, ADTerms1Sub, ADTerms2Sub, 0
            resultMSCheck = self.multisetEquivalenceCheck(ADTerms1Sub, ADTerms2Sub)
            if not resultMSCheck[0]:
                # Not equivalent, stop the check and set equivalence to False.
                equivalence = False
                return equivalence, ADTerms1Sub, ADTerms2Sub, 0

            # If not finished yet, perform check a level deeper.
            equivalence, deeperADTerms1Sub, deeperADTerms2Sub, totalLevenshteinDistance = self.recursiveComparison(
                ADTerms1Sub, ADTerms2Sub, continueCheck, equivalence)
        # After all levels are checked, go back up out of recursion and check parent-child relationship.
        if equivalence:
            parentChildCheck = self.parentChildCheck(ADTerms1Sub, ADTerms2Sub, deeperADTerms1Sub, deeperADTerms2Sub)
        else:
            # If already found that at this point the two ADTerms are not equivalent, set to False.
            parentChildCheck = False

        # Check parent-child relationship with current ADTerms substrings and the deeper level ADTerms substrings. Match them.
        if not parentChildCheck:
            # If parentChildCheck has failed, set equivalence to False.
            equivalence = False

        # Add new Levenshtein Distance to total.
        totalLevenshteinDistance += resultMSCheck[1]

        # Return with four variables: equivalence, the two needed subADTerms to further compare and the total Levenshtein Distance so far.
        return equivalence, ADTerms1Sub, ADTerms2Sub, totalLevenshteinDistance

    def compareADTerms(self, ADTerms1: str, ADTerms2: str) -> Tuple[bool, int]:
        """
        Determines whether two ADTerms are equivalent to each other by comparing the two. Includes check with equivalence threshold using the Levenshtein Distance.

        :param ADTerms1: ADTerm to compare with.
        :param ADTerms2: ADTerm to compare with.
        :return: `bool`, `int`/`None`: `True` and total Levenshtein Distance (`int`) if equivalent, `False` and `None` otherwise.

        Note: *This function is called from the `ADT` class using `compareADTerms(...)`, and should therefore not be called from the `CompADTerms` class.*
        """
        # Set variables continueCheck and equivalence to True.
        # We determine equivalence by finding proof that these two ADTerms are NOT equivalent, not the other way around.
        continueCheck = True
        equivalence = True
        totalLevenshteinDistance = 0

        # If first character of both ADTerms is a symbol, we firstly determine equivalence of these symbols before we
        # start a recursive comparison of Multisets within the ADTerms.
        if ADTerms1[0] != "[" and ADTerms2[0] != "[":
            resultMSCheck = self.multisetEquivalenceCheck(ADTerms1, ADTerms2)
            if not resultMSCheck[0]:
                # If at any time proof is found that the given ADTerms are not equivalent, disable continueCheck.
                continueCheck = False
                return False, 0
            totalLevenshteinDistance += resultMSCheck[1]
        # If first character is not a symbol, or symbols are equivalent, start recursive comparison.
        result = self.recursiveComparison(ADTerms1, ADTerms2, continueCheck, equivalence)

        # After recursive comparison, check whether the comparison resulted in equivalence or not.
        totalLevenshteinDistance += result[3]
        if not result[0]:
            return False, 0
        else:
           return True, totalLevenshteinDistance

    def changeLevenshteinErrorMargin(self, newValue: float) -> bool:
        """
        Changes Levenshtein Distance equivalence threshold value if new value is between 0.0 and 1.0.

        :param newValue: New value of Levenshtein Distance equivalence threshold.
        :return: `bool`: `True` if value changed successfully, `False` otherwise.

        Note: *This function is called from the `ADT` class using `changeLevenshteinErrorMargin(...)`, and should therefore not be called from the `CompADTerms` class.*
        """
        # Changes Levenshtein Distance equivalence threshold with a new value. This value must be in [0, 1].
        if float(newValue) >= 0.0 or float(newValue) <= 1.0:
            self.ADT.LSEquivalenceThreshold = float(newValue)
            return True
        return False