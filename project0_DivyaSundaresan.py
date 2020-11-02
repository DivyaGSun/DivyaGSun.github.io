#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:47:29 2020

@author: Divya
Tic Tac Toe game
"""

import numpy as np
import random
import copy

class Board:
    '''Creates Board items and how to fill them'''
    def __init__(self,m,n):
        '''new board that is made out of numpy array empty ='-' '''
        self.board = np.full((m, n), '-')
        self.tempboard = copy.deepcopy(self.board[:])

    def getBoard(self):
        return self.board
    def printBoard(self):
        print( self.board)

    def printBoard_coords(self):
            '''prints an example board with coordinates for 3x3, so players can reference'''
            coord_board = np.array([['(0,0)','(0,1)','(0,2)'],
                                     ['(1,0)','(1,1)','(1,2)'],
                                     ['(2,0)','(2,1)','(2,2)']],dtype=object)
            print(coord_board)


    def valid_move(self,x,y,m,n):
       '''checks if spot is filled, determing if the player can move there'''
       if x<m and y<n:
           #print('ye')
           return True

       return False
    def valid_spot(self,x,y,temparr):
        #print(temparr)
        #print(x,y)
       # print(self.board[x][y])
        if temparr[x][y] == '-':
            #print('iii')
            return True
        return False

  ##--------------Filling board---------------------------
      #there are two ways to fill either the computer randomly picks or the
      #player gives an input


    def computer_fill_board(self,m,n,k,ai):
        '''The computer checks all possible open locations then randomly
        selects a spot to fill with 'O'.\n
        Returns:the coordinates the computer selected
        Addionally Prints an updated board with the computer spot filled'''
        comp_choice = []
        for i in range(m):
            for j in range(n):
                if self.board[i][j] == '-':
                    comp_choice.append((i, j))
        if ai == 0:
            computer_coord = random.choice(comp_choice)
            self.board[(computer_coord)] = 'O'
            self.printBoard()
            return self.board, computer_coord
        elif ai ==1:
            for i in comp_choice:
                #print(comp_choice)
                self.tempboard = copy.deepcopy(self.board[:])
                #print(i)
                x,y = i
                #print(x,y)
                #print(k)
                if self.check_win(x,y,k,marker ='O',board_type=1):
                    computer_coord = i
                    #print(computer_coord,'W')
                    self.board[(computer_coord)] = 'O'
                    self.printBoard()
                    return self.board, computer_coord
            
            #print('random pick')
            computer_coord = random.choice(comp_choice)
            self.board[(computer_coord)] = 'O'
            self.printBoard()
            return self.board, computer_coord
        elif ai ==2:
            for i in comp_choice:
                #print(comp_choice)
                self.tempboard = copy.deepcopy(self.board[:])
                #print(i)
                x,y = i
                #print(x,y)
                #print(k)
                if self.check_win(x,y,k,marker ='O',board_type=1):
                    computer_coord = i
                    #print(computer_coord,'W')
                    self.board[(computer_coord)] = 'O'
                    self.printBoard()
                    return self.board, computer_coord
            for i in comp_choice:
                #print(comp_choice)
                self.tempboard = copy.deepcopy(self.board[:])
                #print(i)
                x,y = i
                #print(x,y)
                #print(k)
                if self.check_win(x,y,k,marker ='X',board_type=1):
                    computer_coord = i
                    #print(computer_coord,'W')
                    self.board[(computer_coord)] = 'O'
                    self.printBoard()
                    return self.board, computer_coord
            #print('random pick')
            computer_coord = random.choice(comp_choice)
            self.board[(computer_coord)] = 'O'
            self.printBoard()
            return self.board, computer_coord


    def player_fill_board(self,x,y,m,n):
        '''The player gives an input of x or y.
        Function checks if that spot is valid through previous valid_move
        function, it then gives you one more chance to enter a valid number
        and then will update the board.

        Returns updated self.printBoard()'''

        self.board[(x,y)] = 'X'
        return self.printBoard()

##-----------Determining winners------------------
        #Trying to find a way to combine comp is winner and player is winner
        #b/c they are repetive which is uneccesary.But for now they are
        #essentially checking if the player or computer won, should probably
        #be moved to game class

#forward diagonal sequence
    def forward_diag(self,x,y,marker,board_type):
        i,j = x,y
        if board_type == 0:
            seq = np.diagonal(self.board, offset=(j - i))
        else:
             self.tempboard[x][y] = marker
             seq = np.diagonal(self.tempboard, offset=(j - i))
        return seq

#backwords diagonal sequence
    def backwords_diag(self,x,y,marker,board_type):
        i,j = x,y
        if board_type == 0:
            seq = np.diagonal(np.rot90(self.board), offset=-self.board.shape[1] + (j + i) + 1)
        else:
            self.tempboard[x][y] = marker
            seq = np.diagonal(np.rot90(self.tempboard), offset=-self.tempboard.shape[1] + (j + i) + 1)
        return seq
    def horizontal(self,x,y,marker,board_type):
        if board_type == 0:
            seq = self.board[x]
        else: 
            self.tempboard[x][y] = marker
            seq = self.tempboard[x]
        return seq
    def vertical(self,x,y,marker,board_type):
        if board_type == 0:
            seq = self.board[:,y]
        else:
            self.tempboard[x][y] = marker
            seq = self.tempboard[:,y]
        return seq
#getting horizontal, vertical, diagonal, rev-diagonal sequence
    def get_lists(self,x,y,marker,board_type):
        seq_list = []
        seq_list.append(self.horizontal(x,y,marker,board_type))
        seq_list.append(self.vertical(x,y,marker,board_type))
        seq_list.append(self.forward_diag(x,y,marker,board_type))
        seq_list.append(self.backwords_diag(x,y,marker,board_type))
        return seq_list
#do any sequences match the k-length  
    def match_k_length(self,row,k,marker):
        max_l =[]
        #print(row)
        counter =1 
        for i in range(len(row)):
            #print(sq)
            if i < len(row)-1 and row[i] == marker and row[i+1] == marker:
                counter += 1
            else: 
                counter = 1
            #print(counter)
            max_l.append(counter)
        if max(max_l) >= k:
            return 1
        return 0 
    
    def check_win(self,x,y,k,marker,board_type):
        win_list = []
        sequences = self.get_lists(x,y,marker,board_type)
        #print(sequences)
        #print(k)
        for i in sequences:
            win_list.append(self.match_k_length(i, k=k, marker = marker))
        if any(win_list) ==1:
            #print('trueW')
            return True
        return False
##-----------------------------------------------
class interactive_games:
    '''This class displays board class, and instructions for game '''
    def __init__(self,m,n):
        """Each game needs a board"""
        self.game = Board(m,n)

    def display_instructions(self,m,n,k):
        '''Instructions for the game'''
        print('------------------------------------------------')
        print("\n\nWelcome to Tic Tac Toe, you are always 'X'\n")
        print("Here is an example of a board with coordinates for a 3X3 board, based on your board size specify appropriate coordinates for the location of 'X'\n")
        self.game.printBoard_coords()
        print("\nWhen promted, enter the coordinates ex:) selecting (0,0) as 0 0\n")
        print("This is how the empty board will appear")
        self.game.printBoard()
        print("\n\nGood Luck!\n")
        print('------------------------------------------------')

    def player_game_over(self,x,y,k, marker ='X',board_type=0):
        return self.game.check_win(x,y,k,marker,board_type)
    def comp_game_over(self,x,y,k, marker = 'O',board_type=0):
        return self.game.check_win(x,y,k,marker,board_type)
    def update_board_comp(self,m,n,k,ai):
        return self.game.computer_fill_board(m,n,k,ai)
    def update_board_player(self,x,y,m,n):
        return self.game.player_fill_board(x,y,m,n)
    #def player_starts(self):
        
        
#--------randomly determing who starts------------
class player:
    '''Determines who starts computer or player'''
    def player_order(self):
        '''If returns 0 player starts, else computer starts'''
        player_selection = random.choice([0, 1])
        if player_selection == 0:
            return 0
        else:
            return 1

#------main --------
def play_game():
    '''play game function that runs while one game is being played calls the
    game class.This function has a primary while loop which is determined
    by turns(move_count). This is 9 b/c I am going up in increments of two
    but in the last round stop after the first player goes. it is then
    decided if that player wins or a tie occured. There is a break after a
    tie, loss, win, which feeds into main function'''
    
    m = int(input('pick the amount of rows you want on board:'))
    n = int(input('pick the amount of columns you want on board:'))
    k = int(input('length of sequence horizontally, verically, or diagonally that leads to win\n *This must be less than or equal to m or n (whichever is greater) to win:'))
    ai = int(input('pick ai level(each level increases difficulty) either 0,1, or 2:'))
    boards = Board(m,n)
    #boards.printBoard()
    play = interactive_games(m,n)
    player_start = player()
    play.display_instructions(m,n,k)
    move_count = 0
    temparr = boards.getBoard()
    if player_start.player_order() == 0:
        #player starts
        print('You have been randomly chosen to start first')
        while move_count <= m*n:
             move_count += 2
             #print(m*n, move_count)
             #get valid input through while loop
             while True:
                 x,y = [int(x) for x in input("Pick your spot for 'X', Enter two values seperated by a space:").split()]
                 if not boards.valid_move(x,y,m,n):
                     print('\nNot valid move')
                     continue
                 if not boards.valid_spot(x,y,temparr):
                     print('\nspot taken')
                     continue
                 else:
                     break
             play.update_board_player(x,y,m,n)
             print("\n")
             if play.player_game_over(x,y,k):
                 print('You Won, NICE work')
                 break
             if move_count >= m*n:
                 if play.player_game_over(x,y,k):
                     print('You Won, NICEE work')
                     break
                 else:
                     print("It's a tie!")
                     break
             #grab array from previous round to check for valid values in 
             #next round
             temparr, computer_coords= play.update_board_comp(m,n,k,ai)
             x, y = computer_coords
             print ('computer picked:',computer_coords,'\n')
             if play.comp_game_over(x,y,k):
                 print('You lost!')
                 break
    else:
        #computer starts opposite order
        #not ending game on k win 
        print('You have been randomly chosen to start second\n')
        while move_count <= m*n :
             move_count += 2
             #print(m*n, move_count)
             temparr,computer_coords = play.update_board_comp(m,n,k,ai)
             x,y = computer_coords
             print ('computer picked:',computer_coords,'\n')
             if play.comp_game_over(x,y,k):
                 print('You lost!')
                 break
             if move_count >= m*n:
                 if play.comp_game_over(x,y,k):
                     print('You Lost, sorry')
                     break
                 else:
                     print("It's a tie!")
                     break
            # x,y = [int(x) for x in input("Pick your spot for 'X', Enter two values seperated by a space:").split()]
             while True:
                  x,y = [int(x) for x in input("Pick your spot for 'X', Enter two values seperated by a space:").split()]
                  if not boards.valid_move(x,y,m,n):
                     print('\nNot valid move')
                     continue
                  if not boards.valid_spot(x,y,temparr):
                     print('\nspot taken')
                     continue
                  else:
                     break
             play.update_board_player(x,y,m,n)
             print("\n")
             if play.player_game_over(x,y,k):
                 print('You Won, NICE work')
                 break

def main():
    '''replay or nah'''
    answer = 'y'
    while answer == 'y':
        play_game()
        answer = input("play again? answer y to play, anything else to quit:")
    print('Byee, see you soon!')
#Executer
if __name__ == '__main__':main()