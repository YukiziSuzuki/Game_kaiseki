# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:30:11 2023

@author: suzuki
"""

import copy
import numpy as np

class Node:
    def __init__(self, state):
        self.state = np.array(state)
        self.children = np.array([])

def generate_game_tree():
    # 初期盤面の生成
    initial_state = np.array([["〇","〇","〇","_","_","_","■","■","■"],["〇","〇","〇","_","_","_","■","■","■"],["〇","〇","〇","_","_","_","■","■","■"],"flag","〇"])

    # 初期ノードの作成
    root = Node(initial_state)

    # ゲーム木の構築
    build_game_tree(root, '〇')

    return root


def is_game_over(state):
    # 勝利条件のチェック
    if state[0][8]=="〇" and state[0][7]=="〇" and state[0][6]=="〇" and state[1][8]=="〇" and state[1][7]=="〇" and state[1][6]=="〇" and state[2][8]=="〇" and state[2][7]=="〇" and state[2][6]=="〇":
        return 1
    elif state[0][0]=="■" and state[0][1]=="■" and state[0][2]=="■" and state[1][0]=="■" and state[1][1]=="■" and state[1][2]=="■" and state[2][0]=="■" and state[2][1]=="■" and state[2][2]=="■":
        return -1

    return 0


def build_game_tree(node, player):

    print(node.state)
    # ゲームが終了しているかどうかをチェック
    if is_game_over(node.state)==1:
        node.state[3]="W"
        print(node.state)
        print("end_WIN")
        return
    elif is_game_over(node.state)==-1:
        node.state[3]="L"
        print(node.state)
        print("end_LOSE")
        return

    data_0=[]
    data_1=[]
    data_2=[]
    # 空のマス目に対して、次のプレイヤーの手を配置する

    if player=="〇":
        for i in range(9):
            if node.state[0][i]==player:
                data_0.append(i)
            if node.state[1][i]==player:
                data_1.append(i)
            if node.state[2][i]==player:
                data_2.append(i)

        for i in data_0:
            new_state = copy.deepcopy(node.state)
            new_state[4]="〇"
            for j in range(i,9):
                if new_state[0][j]=="_":
                    new_state[0][j]=player
                    new_state[0][i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children=np.array(child)
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break


        for i in data_1:
            new_state = copy.deepcopy(node.state)
            new_state[4]="〇"
            for j in range(i,9):
                if new_state[1][j]=="_":
                    new_state[1][j]=player
                    new_state[1][i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children=np.array(child)
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break


        for i in data_2:
            new_state = copy.deepcopy(node.state)
            new_state[4]="〇"
            for j in range(i,9):
                if new_state[2][j]=="_":
                    new_state[2][j]=player
                    new_state[2][i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children=np.array(child)
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break

    if player=="■":
        for i in range(8,-1,-1):
            if node.state[0][i]==player:
                data_0.append(i)
            if node.state[1][i]==player:
                data_1.append(i)
            if node.state[2][i]==player:
                data_2.append(i)


        for i in data_0:
            new_state = copy.deepcopy(node.state)
            new_state[4]="■"
            for j in range(i,-1,-1):
                if new_state[0][j]=="_":
                    new_state[0][j]=player
                    new_state[0][i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children=np.array(child)
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break


        for i in data_1:
            new_state = copy.deepcopy(node.state)
            new_state[4]="■"
            for j in range(i,-1,-1):
                if new_state[1][j]=="_":
                    new_state[1][j]=player
                    new_state[1][i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children=np.array(child)
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break


        for i in data_2:
            new_state = copy.deepcopy(node.state)
            new_state[4]="■"
            for j in range(i,-1,-1):
                if new_state[2][j]=="_":
                    new_state[2][j]=player
                    new_state[2][i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children=np.array(child)
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break


    # 次のプレイヤーに交代して再帰的にゲーム木を構築
    #build_game_tree(child, '〇' if player == '■' else '■')



def retraction_analysis(node):

    for child in node.children:
        retraction_analysis(child)

    if node.state[3]!="flag":
        return


    if node.state[4]=="〇":
        node.state[3]="L"
        for child in node.children:
            if child.state[3]=="W":
                node.state[3]="W"
                return
    elif node.state[4]=="■":
        node.state[3]="W"
        for child in node.children:
            if child.state[3]=="L":
                node.state[3]="L"

def print_game_tree(node, depth=0):
    # 盤面を表示
    #print('  ' * depth + str(node.state))
    for i in range(4):
        file.write(str(node.state[i])+"\n")
    file.write("---------"+str(depth)+"\n")

    # 子ノードに再帰的に適用
    for child in node.children:
        print_game_tree(child, depth + 1)



# ゲーム木の生成と表示
game_tree = generate_game_tree()

retraction_analysis(game_tree)

file=open("ぴょんぴょん将棋＿全盤面.txt", "w")
print_game_tree(game_tree)
file.close()