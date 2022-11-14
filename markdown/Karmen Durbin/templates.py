###########（っ＾▿＾）Templates for Patterns ###########

##### ( ≖.≖) EASY ######
#! Fixed Window, if statement, checking the curr idx against the val of k

####### ʕ•́ᴥ•̀ʔっ Sliding Window Easy Sudo ###### 
#* initialize variables
#* try to extend the window, THIS IS OUR FOR LOOP
#* try to move the window for a fixed window, THIS IS OUR IF STATEMENT
#* shrink the window
#* return res


def find_averages_of_subarrays(K, arr):
  result = []
  win_sum, win_start = 0.0, 0
  #* grow the window
  for win_end in range(len(arr)):
    win_sum += arr[win_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    #* shrink the window
    if win_end >= K - 1:
      result.append(win_sum / K)  # calculate the average
      win_sum -= arr[win_start]  # subtract the element going out
      win_start += 1  # slide the window ahead

  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))
main()


##### ( ≖.≖) MEDIUM & HARD ######
#! Dynamic Window, while loop, checking (the curr val/idx) against a condition to ensure it is true

####### ʕ•́ᴥ•̀ʔっ Sliding Window Medium/Hard Sudo ###### 
#* Initialize the problem
#* Try to grow the window at each iteration, this is our IF STATEMENT
#* Try to shrink the window, This is our WHILE LOOP... while ____ is ___, shrink the window (why shrink it?) 
#* conditional 
#* return res




