import copy

# ノードクラスを定義します。各ノードはゲームの特定の状態を表し、その子ノードを持ちます
class Node:
    def __init__(self, state):
        self.state = state
        self.children = []
        
 # ゲーム木を生成します。初期状態から始めて、可能なすべてのゲームの状態を探索します。       
def generate_game_tree():
    # 初期盤面の生成
    initial_state = ["〇","〇","〇","_","_","_","■","■","■","flag","〇"]
    
    # 初期ノードの作成
    root = Node(initial_state)
    
    # ゲーム木の構築
    build_game_tree(root, '〇')
    
    return root
    
# ゲーム木を構築します。現在のノードと次のプレイヤーを引数として取り、可能なすべての次の状態に対して子ノードを作成します。
def build_game_tree(node, player):
    
    print(node.state)
    
    # ゲームが終了しているかどうかをチェック
    if node.state[8]=="〇" and node.state[7]=="〇" and node.state[6]=="〇":
        node.state[9]="W"
        print(node.state)
        print("end_WIN")
        return
    elif node.state[0]=="■" and node.state[1]=="■" and node.state[2]=="■":
        node.state[9]="L"
        print(node.state)
        print("end_LOSE")
        return
    
    data=[]
    # 空のマス目に対して、次のプレイヤーの手を配置する

    if player=="〇":
        for i in range(9):
            if node.state[i]==player:
                data.append(i)
                
        for i in data:
            new_state = copy.deepcopy(node.state)
            new_state[10]="〇"
            for j in range(i,9):
                if new_state[j]=="_":
                    new_state[j]=player
                    new_state[i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children.append(child)
                    # 次のプレイヤーに交代して再帰的にゲーム木を構築
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break
                    
    if player=="■":
        for i in range(8,-1,-1):
            if node.state[i]==player:
                data.append(i)
                
        for i in data:
            new_state = copy.deepcopy(node.state)
            new_state[10]="■"
            for j in range(i,-1,-1):
                if new_state[j]=="_":
                    new_state[j]=player
                    new_state[i]="_"
                    # 新しいノードを作成し、現在のノードの子とする
                    child = Node(new_state)
                    node.children.append(child)
                    # 次のプレイヤーに交代して再帰的にゲーム木を構築
                    build_game_tree(child, '〇' if player == '■' else '■')
                    break

# ゲームが終了しているかどうかを判断します。勝利条件を満たしている場合は1または-1を返し、それ以外の場合は0を返します。                
def is_game_over(state):
    # 勝利条件のチェック
    if state[8]=="〇" and state[7]=="〇" and state[6]=="〇":
        return "1"
    elif state[0]=="■" and state[1]=="■" and state[2]=="■":
        return "-1"
    
    return "0"

# ゲーム木を表示します。各ノードの状態を表示し、その子ノードに再帰的に適用します。
def print_game_tree(node, depth=0):
    # 盤面を表示
    #print('  ' * depth + str(node.state))
    for i in range(11):
        file.write(str(node.state[i]))
    file.write("---------"+str(depth)+"\n")
    
    # 子ノードに再帰的に適用
    for child in node.children:
        print_game_tree(child, depth + 1)
        
        
# 後退解析を行います。各ノードが勝ちか負けかを決定します。        
def retraction_analysis(node):
    
    for child in node.children:
        retraction_analysis(child)
        
    if node.state[9]!="flag":
        return
    
    if node.state[10]=="〇":
        node.state[9]="L"
        for child in node.children:
            if child.state[9]=="W":
                node.state[9]="W"
                return
    elif node.state[10]=="■":
        node.state[9]="W"
        for child in node.children:
            if child.state[9]=="L":
                node.state[9]="L"
    
# ゲーム木の生成と表示
game_tree = generate_game_tree()

retraction_analysis(game_tree)

file=open("ぴょんぴょん将棋＿盤面.txt", "w")
print_game_tree(game_tree)
file.close()
