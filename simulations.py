#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:44:19 2020

@author: Divya
"""
#doing simulations
import numpy as np
import copy
import random
class Board:
    def __init__(self,m,n):
            '''new board that is made out of numpy array empty ='-' '''
            self.board = np.full((m, n), '-')
            self.tempboard = copy.deepcopy(self.board[:])
    def getBoard(self):
        return self.board
    def computer_fill_board(self,m,n,k,marker,ai):
            '''The computer checks all possible open locations then randomly
            selects a spot to fill with 'O'.\n
            Returns:the coordinates the computer selected
            Addionally Prints an updated board with the computer spot filled'''
            marker_list = ['O','X']
            if marker in marker_list: marker_list.remove(marker)
            other_player_sym = marker_list[0]
            comp_choice = []
            for i in range(m):
                for j in range(n):
                    if self.board[i][j] == '-':
                        comp_choice.append((i, j))
            if ai == 0:
                computer_coord = random.choice(comp_choice)
                self.board[(computer_coord)] = marker
                #self.printBoard()
                return self.board, computer_coord
            elif ai ==1:
                for i in comp_choice:
                    #print(comp_choice)
                    self.tempboard = copy.deepcopy(self.board[:])
                    #print(i)
                    x,y = i
                    #print(x,y)
                    #print(k)
                    if self.check_win(x,y,k,marker =marker,board_type=1):
                        computer_coord = i
                        #print(computer_coord,'W')
                        self.board[(computer_coord)] = marker
                        #self.printBoard()
                        return self.board, computer_coord

                #print('random pick')
                computer_coord = random.choice(comp_choice)
                self.board[(computer_coord)] = marker
                #self.printBoard()
                return self.board, computer_coord
            elif ai ==2:
                for i in comp_choice:
                    #print(comp_choice)
                    self.tempboard = copy.deepcopy(self.board[:])
                    #print(i)
                    x,y = i
                    #print(x,y)
                    #print(k)
                    if self.check_win(x,y,k,marker =marker,board_type=1):
                        computer_coord = i
                        #print(computer_coord,'W')
                        self.board[(computer_coord)] = marker
                        #self.printBoard()
                        return self.board, computer_coord
                for i in comp_choice:
                    #print(comp_choice)
                    self.tempboard = copy.deepcopy(self.board[:])
                    #print(i)
                    x,y = i
                    #print(x,y)
                    #print(k)
                    if self.check_win(x,y,k,marker = other_player_sym, board_type=1):
                        computer_coord = i
                        #print(computer_coord,'W')
                        self.board[(computer_coord)] = marker
                        #self.printBoard()
                        return self.board, computer_coord
                #print('random pick')
                computer_coord = random.choice(comp_choice)
                self.board[(computer_coord)] = marker
                #self.printBoard()
                return self.board, computer_coord
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
class player:
    '''Determines who starts computer or player'''
    def player_order(self):
        '''If returns 0 player starts, else computer starts'''
        player_selection = random.choice([0, 1])
        if player_selection == 0:
            return 0
        else:
            return 1
def play_game(m,n,k,ai_1,ai_2):
    m= m
    n= n
    k= k
    marker1 = 'X'
    marker2 = 'O'
    boards = Board(m,n)
#     player_list = [ai_1,ai_2]
#     player1 = random.choice(player_list)
#     player2 = player_list.pop(player1)
    move_count = 0
    temparr = boards.getBoard()
    player_start = player()
    if player_start.player_order() == 0:
        #first ai starts
        while move_count <= m*n:
            move_count += 2
            #print(move_count)
            temparr,computer_coords = boards.computer_fill_board(m,n,k,marker1,ai=ai_1)
            x,y = computer_coords
            if boards.check_win(x,y,k,marker1,board_type = 0):
                return 1
                break
             #grab array from previous round to check for valid values in 
             #next round
            if move_count >= m*n:
                return 0
                break
            #print(temparr)
            temparr,computer_coords = boards.computer_fill_board(m,n,k,marker2,ai=ai_2)
            x, y = computer_coords
            if boards.check_win(x,y,k,marker2,board_type = 0):
                return 2
                break
    else:
        #second ai starts
        while move_count <= m*n:
            move_count += 2
            #print(move_count)
            temparr,computer_coords = boards.computer_fill_board(m,n,k,marker2,ai=ai_2)
            x,y = computer_coords
            if boards.check_win(x,y,k,marker2,board_type = 0):
                return 2
                break
             #grab array from previous round to check for valid values in 
             #next round
            if move_count >= m*n:
                return 0
                break
            #print(temparr)
            temparr,computer_coords = boards.computer_fill_board(m,n,k,marker1,ai=ai_1)
            x, y = computer_coords
            if boards.check_win(x,y,k,marker1,board_type = 0):
                return 1
                break