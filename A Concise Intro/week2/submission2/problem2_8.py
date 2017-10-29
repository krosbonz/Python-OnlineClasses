def problem2_8(temp_list):
    #for i in temp_list:
        sum_ = 0
        for i in temp_list:
            sum_ = sum_ + i
        avg_ = sum_/len(temp_list) 
        print("Average:", avg_)
        print("High:", max(temp_list))
        print("Low:", min(temp_list))