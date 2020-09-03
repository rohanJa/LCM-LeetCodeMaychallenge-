'''
    Rules - 
    - one driver is needed for driving the boat to the other side
    - if cannibals are more than the missionaries on the other side they will eat the human.
    - So cannibals should be less than the human.
    Approach-
        Using BFS transfer 3 cannibals and 3 missionaries to other side of the bank
'''
def solution(initial_state, goal_state):
    state = [initial_state]     #give the state of the cannibals
    directions = {1:0,0:1}      #This will give the direction of the boat
    history = set()
    cost = 0
    history.add(initial_state)
    while(len(state)>0):
        print(state)
        cost += 1
        length = len(state)
        for i in range(0,length):
            selected_state = state.pop(0)
            print("selected_state: {}".format(selected_state))
            if(selected_state==goal_state):
                print("End reached")
                break
            else:
                missionary_state, canibal_state,curr_state_direction = selected_state
                opposite_state_M, opposite_state_P,opposite_state_direction = 3 - missionary_state, 3 - canibal_state, directions[curr_state_direction]
                #If the boat is on left side of bank
                if((missionary_state>=canibal_state or missionary_state==0) and (opposite_state_M>=opposite_state_P or opposite_state_M==0) and curr_state_direction==1):
                    if(missionary_state>0 and (missionary_state-1,canibal_state,opposite_state_direction) not in history):
                        state.append((missionary_state-1,canibal_state,opposite_state_direction))
                        history.add((missionary_state-1,canibal_state,opposite_state_direction))
                    if(canibal_state>0 and (missionary_state,canibal_state-1,opposite_state_direction) not in history):
                        state.append((missionary_state,canibal_state-1,opposite_state_direction))
                        history.add((missionary_state,canibal_state-1,opposite_state_direction))
                    if(missionary_state>1 and (missionary_state-2,canibal_state,opposite_state_direction) not in history):
                        state.append((missionary_state-2,canibal_state,opposite_state_direction))
                        history.add((missionary_state-2,canibal_state,opposite_state_direction))
                    if(canibal_state>1 and (missionary_state,canibal_state-2,opposite_state_direction) not in history):
                        state.append((missionary_state,canibal_state-2,opposite_state_direction))
                        history.add((missionary_state,canibal_state-2,opposite_state_direction))
                    if(canibal_state>0 and missionary_state>0 and (missionary_state-1,canibal_state-1,opposite_state_direction) not in history):
                        state.append((missionary_state-1,canibal_state-1,opposite_state_direction))
                        history.add((missionary_state-1,canibal_state-1,opposite_state_direction))
                #If the boat is on right side of bank
                if((missionary_state>=canibal_state or missionary_state==0) and (opposite_state_M>=opposite_state_P or opposite_state_M==0) and curr_state_direction==0):
                    if(opposite_state_M>0 and (missionary_state+1,canibal_state,opposite_state_direction) not in history):
                        state.append((missionary_state+1,canibal_state,opposite_state_direction))
                        history.add((missionary_state+1,canibal_state,opposite_state_direction))
                    if(opposite_state_P>0 and (missionary_state,canibal_state+1,opposite_state_direction) not in history):
                        state.append((missionary_state,canibal_state+1,opposite_state_direction))
                        history.add((missionary_state,canibal_state+1,opposite_state_direction))
                    if(opposite_state_M>1 and (missionary_state+2,canibal_state,opposite_state_direction) not in history):
                        state.append((missionary_state+2,canibal_state,opposite_state_direction))
                        history.add((missionary_state+2,canibal_state,opposite_state_direction))
                    if(opposite_state_P>1 and (missionary_state,canibal_state+2,opposite_state_direction) not in history):
                        state.append((missionary_state,canibal_state+2,opposite_state_direction))
                        history.add((missionary_state,canibal_state+2,opposite_state_direction))
                    if(opposite_state_M>0 and opposite_state_P>0 and (missionary_state+1,canibal_state+1,opposite_state_direction) not in history):
                        state.append((missionary_state+1,canibal_state+1,opposite_state_direction))
                        history.add((missionary_state+1,canibal_state+1,opposite_state_direction))
    return cost


initial_state = (3,3,1)
final_state = (0,0,0)

print(solution(initial_state,final_state))