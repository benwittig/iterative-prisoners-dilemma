####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Test1' # Only 10 chars displayed.
strategy_name = 'Lull to sleep'
strategy_description = '''Collude on the first move, and collude after any round
they colluded before, and after they collude five times in a row, betray. 
Betray if betrayed.'''

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
        return 'c'
    elif their_history[-1] == 'b' :
        return 'b'
    elif len(my_history) >= 5 :
        if their_history[-5:] == 'ccccc' :
            return 'b'
        else:
            return 'c'
    else:
        return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray after betrayed.
    if test_move(my_history='ccc',
              their_history='ccb', 
              my_score=-500,
              their_score=100,
              result='b'):
         print 'Test passed'
     # Test 2: Betray after they collude five times
    if test_move(my_history='ccccc',
              their_history='ccccc', 
              my_score=0, 
              their_score=0,
              result='b'):
          print 'test passed'             