#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions for Assignment 06 
# Change Log: (Who, When, What)
# Muthu, 2021-Feb-19 , Analyzed starter script and decided on new functions to be added
# Muthu,2021-Feb-19 , Added new functions add_cd 
# Muthu 2021-Feb-20 , Added new function del_cd
# Muthu 2021-Feb-21 , Updated main program and checked whether all functions are being called at right time 
#------------------------------------------#

import os


# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


#Create file if file does not exist
if not os.path.exists(strFileName):
    with open(strFileName, 'w'):pass 

# -- PROCESSING -- #
class DataProcessor:
    
    """Add/Delete new CD Data entered by user to/from the table""" 
    
    def add_cd(strID,strTitle,strArtist):
        """Function to add data entered by user to the 2D table

        Write CD Details as a dictionary entry .
        Add this dictionary to the 2D list .

        Args:
            strID (string ): ID for the CD entered by user
            strTitle (string ) : Title for the CD entered by user
            strArtist ( String ) : Artist name for the CD entered by user 
            
        Returns:
            None.
        """
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        
    def delete_CD(intIDDel,lstTbl):
        """Function to delete a row identified by user from 2D table

        Checks if there is a match between the ID entered by the user and the ID present in the list .
        If there is a match delete the row that matches the ID .
        Display the latest content in the table .

        Args:
            intIDDel (Integer) : The CD ID entered by user 
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """     
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed\n\n')
        else:
            print('Could not find this CD!')
        IO.show_inventory(lstTbl)
        
         

class FileProcessor:
    
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(strFileName, lstTbl):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        lstTbl.clear()  # this clears existing data and allows to load data from file
        objFile = open(strFileName, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            lstTbl.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(strFileName,lstTbl):
        """Function to write data from list of dictionaries to a file

        Reads the data from 2D table row by row 
        Create a list with values from the key value pair of each row
        Join the contents of this list with a "," seperator 
        Write the list to the file
      
        Args:
            file_name (string): name of file used to write the data
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
                                        
 
# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""
    
    def ask_details():
        """Ask 3 different data from user ( ID , title , artist)

        Args:
            None.

        Returns:
            CD ID , CD title and Artist name 
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return(strID,strTitle,strArtist)
        

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\t\t\tCD Title\t\t\t(by: Artist)\n')
        for row in table:
            print('{}\t\t\t{}\t\t\t\t(by:{})'.format(*row.values()))
        print('======================================\n\n')



# 1. When program starts, read in the currently saved Inventory

FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled : ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu: ')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID,strTitle,strArtist=IO.ask_details()
        
        # 3.3.2 Add item to the table
        DataProcessor.add_cd(strID,strTitle,strArtist)
        
        IO.show_inventory(lstTbl)        
        continue  # start loop back at top.
        
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_CD(intIDDel,lstTbl)    
        continue  # start loop back at top.
        
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)               
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




