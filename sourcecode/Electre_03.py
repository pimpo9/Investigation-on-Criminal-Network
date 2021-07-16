import csv
import math
from tabulate import tabulate
from tkinter import *
from tkinter import filedialog

root=Tk()
root.title('Major Project')

def openfunc():
     
     root.filename=filedialog.askopenfilename(initialdir="/",title="SELECT A FILE")
     
          
     
     my_label=Label(root,text=root.filename).pack()
     
#####################################################################        DECISION MATRIX CONSTRUCTION            #############################################################################################     
     data = []
     with open(root.filename) as csvfile:
          reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
          for row in reader:                                         # each row is a list
               data.append(row)
     #print("Printing the converted csv file in list format")        
     #print(data)                 print data in list format 

     #Count the rows and columns in .csv file
     rows=len(data)
     columns=len(data[0])
     print("No of rows in the decision matrix=",rows)
     print("No of columns in decision matrix=",columns)




     #Specify the criteria's and append it to the criteria_list
     no_criteria=int(input("Specify the number of criteria's : "))
     criteria_list =[]
     print("Please append your criteria's in the list")

     for i in range(no_criteria): 
         criteria_list.append(input())
     print("Criteria list is given below")
     print(criteria_list)




     #Mention the alternatives and append it to the alternatives list
     alternatives=[]
     no_alternatives=int(input("Specify the number of alternatives:"))
     print("Append the alternatives in the list")
     for i in range(no_alternatives):
         alternatives.append(input())
     print("Alternatives list is given below")
     print(alternatives)





     #Converted the .csv file in decision matrix,combined with crireia_list and alternatives,also display it in tabular form
     decision_matrix=[]
     for i in range((rows+1)):
          decision_matrix.append([])
          for j in range((columns+1)):
               if((i==0)&(j==0)):
                    decision_matrix[i].append("*")
               elif((i==0)&(j!=0)):
                    decision_matrix[i].append(criteria_list[j-1])
               elif((i!=0)&(j==0)):
                    decision_matrix[i].append(alternatives[i-1])
               else:
                    decision_matrix[i].append(float(data[i-1][j-1]))
     print(tabulate(decision_matrix,tablefmt="grid"))



     

     #Mention the weights of each criteria,remember to mention the weights in the same order as of the criteria's appended in criteria_list  

     print("Mention the weights for each respective criteria in the same order as the criteria's")
     criteria_weight=[]
     for i in range(no_criteria): 
         criteria_weight.append(input())
     print("Weights of criteria's are given below")
     print(criteria_weight)



########################################################################    NORMLAIZATION OF DECISION MATRIX                 ####################################################################################

     #Normalization of decision matrix
     normalize=[]
     for i in range(columns):
          
          sum=0
          for j in range(rows):
              
               sum=sum+math.pow(float(data[j][i]),2.0)
      

          normalize.append(math.sqrt(sum))

     print("Normalized score value for each column is given below")
     print(normalize)





     #Normalized matrix constructed
     normalized_list=[]
     for i in range(rows):
         normalized_list.append([])
         for j in range(columns):
              normalized_list[i].append(float(data[i][j])/normalize[j])

     
     print("Normalized matrix is given below")
     #These statements will display the normalized_list in list format
     #for i in normalized_list:
     #    print(i)

     #Display the normalized matrix in tabular form
     normalize_display=[]
     for i in range((rows+1)):
          normalize_display.append([])
          for j in range((columns+1)):
               if((i==0)&(j==0)):
                    normalize_display[i].append("*")
               elif((i==0)&(j!=0)):
                    normalize_display[i].append(criteria_list[j-1])
               elif((i!=0)&(j==0)):
                    normalize_display[i].append(alternatives[i-1])
               else:
                    normalize_display[i].append(normalized_list[i-1][j-1])
     print(tabulate(normalize_display,tablefmt="grid"))




##############################################################################   WEIGHTING THE NORMALIZED MATRIX   #########################################################################
     
     #Weighting the decision matrix
     weighted_list=[]
     for i in range(rows):
         weighted_list.append([])
         for j in range(columns):
             weighted_list[i].append(float(normalized_list[i][j])*float(criteria_weight[j]))
             
     print("Weighted list is given below")
     #These satements will print the weighted_list in simple iste format
     #for i in weighted_list:
     #    print(i)

     weighted_display=[]
     for i in range((rows+1)):
          weighted_display.append([])
          for j in range((columns+1)):
               if((i==0)&(j==0)):
                    weighted_display[i].append("*")
               elif((i==0)&(j!=0)):
                    weighted_display[i].append(criteria_list[j-1])
               elif((i!=0)&(j==0)):
                    weighted_display[i].append(alternatives[i-1])
               else:
                    weighted_display[i].append(weighted_list[i-1][j-1])
     print(tabulate(weighted_display,tablefmt="grid"))




##############################################################################   CONCORDANCE MATRIX CONSTRUCTION    ###########################################################################     

     #STEP 1  : Intermediate matrix for Concordance matrix

     intermediate_con=[]

     for i in range(no_alternatives):
         intermediate_con.append([])
    
         for k in range(no_alternatives):
             sum=0

             if(i==k):
                sum=0
           
             elif(i!=k):
            
                 for j in range(columns):
                
                      if(weighted_list[i][j]>=weighted_list[k][j]):
                    
                          sum=sum+float(criteria_weight[j])




             intermediate_con[i].append(sum)
             

     print("Intermediate concordance set values are obtained")  
     #for i in intermediate_con:
     #     print(i)
     intermediate_display=[]
     for i in range(no_alternatives+1):
          intermediate_display.append([])
          for j in range(no_alternatives+1):
               if((i==0)&(j==0)):
                    intermediate_display[i].append("*")
               elif((i==0)&(j!=0)):
                    intermediate_display[i].append(alternatives[j-1])
               elif((i!=0)&(j==0)):
                    intermediate_display[i].append(alternatives[i-1])
               else:
                    intermediate_display[i].append(intermediate_con[i-1][j-1])
     print(tabulate(intermediate_display,tablefmt="grid"))
               

     #To count number of values which are not null and sum of values in the matrix
     #to calculate average of the total sum            
     count=0
     total=0
     for i in range(no_alternatives):
         for j in range(no_alternatives):
             if(intermediate_con[i][j]!=0):
                 count=count+1
            
             total=total+intermediate_con[i][j]

     print("Total sum of values in intermediate concordance set=",total)
     print("Total number of non zero values in intermediate concoradance set=",count)
     avg=total/count
     print("Average of the values in intermediate concordance matrix=",avg)

     
     #STEP 2: CONSTRUCTION OF BINARY CONCORDANCE MATRIX 
     #Concordance matrix constructed from intermediate concordance matrix

     concordance_set=[]
     for i in range(no_alternatives):
         concordance_set.append([])
         for j in range(no_alternatives):
             if(intermediate_con[i][j]>=avg):
                 concordance_set[i].append(1)

             else:
                 concordance_set[i].append(0)
     print("Binary concordance matrix")
     #for i in concordance_set:
     #    print(i)

     #to display concordance matrix in table format
     display=[]
     for i in range((no_alternatives)+1):
         display.append([])
         for j in range((no_alternatives)+1):
             if((i==0)&(j==0)):
                 display[i].append("*")

             elif((i==0)&(j!=0)):
                 display[i].append(alternatives[j-1])

             elif((i!=0)&(j==0)):
                 display[i].append(alternatives[i-1])

             else:
                 display[i].append(concordance_set[i-1][j-1])



     print(tabulate(display,tablefmt="grid"))






#############################################################################DISCORDANCE MATRIX PART########################################################################################
     #STEP 1  :   Discordance matrix evaluation part1
     c=-1
     intermediate_discordance=[]

     for i in range(no_alternatives):
          
          for k in range(no_alternatives):
               if (i!=k):
                   c=c+1
                   intermediate_discordance.append([])
                   for j in range(columns):
                        intermediate_discordance[c].append(weighted_list[i][j]-weighted_list[k][j])

     #print("Intermediate discordance part1 values")                     
     #for i in intermediate_discordance:             
     #   print(i)

     
     #STEP 2  :  Intermediate discordance matrix part 2 
     c=-1
     intermediate_don=[]  
     for i in range(no_alternatives):
          intermediate_don.append([])
    
          for k in range(no_alternatives):
    

               if(i==k):
                   sum=0
           
               elif(i!=k):
                   c=c+1
                   #p=min([n for n in intermediate_discordance[c] if n<0])
                   #q=max(abs(ele) for ele in intermediate_discordance[c])
                   #sum=p/q

                   p=min([n for n in intermediate_discordance[c]])
                   l=[]
                   l=[abs(ele) for ele in intermediate_discordance[c]]
                   r=max(l)
                   #q=max(abs(ele) for ele in intermediate_discordance[c])
                   if (r==0):
                       r=0.1
                       
                   
                   sum=p/r
                   #print(abs(sum))




               intermediate_don[i].append(abs(sum))

               

     print("Intermediate discordance set values are obtained")



     #Display the intermediate discoradnce "intermediate_don" matrix   
     #for i in intermediate_don:
     #      print(i)
     intermediatediscordance_display=[]
     for i in range((no_alternatives)+1):
         intermediatediscordance_display.append([])
         for j in range((no_alternatives)+1):
             if((i==0)&(j==0)):
                 intermediatediscordance_display[i].append("*")

             elif((i==0)&(j!=0)):
                 intermediatediscordance_display[i].append(alternatives[j-1])

             elif((i!=0)&(j==0)):
                 intermediatediscordance_display[i].append(alternatives[i-1])

             else:
                 intermediatediscordance_display[i].append(round(intermediate_don[i-1][j-1],6))

     print(tabulate(intermediatediscordance_display,tablefmt="grid"))

     #To count number of values which are not null and sum of values in the matrix
     #to calculate average of the total sum            
     count=0
     total=0
     for i in range(no_alternatives):
          for j in range(no_alternatives):
              if(intermediate_don[i][j]!=0):
                  count=count+1
            
              total=total+intermediate_don[i][j]

     print("Total sum of values in intermediate discordance matrix=",total)
     print("Toatl non zero values=",count)
     avg=total/count
     print("Average of the values in intermediate discordance matrix=",avg)


     #STEP 3 :BINARY DISCORDANCE MATRIX CONSTRUCTION
     discordance_set=[]
     for i in range(no_alternatives):
         discordance_set.append([])
         for j in range(no_alternatives):
             if(intermediate_don[i][j]>=avg):
                 discordance_set[i].append(1)

             else:
                 discordance_set[i].append(0)
     print("Binary discordance matrix")
     #These statements will print it in list format
     #for i in discordance_set:          
     #    print(i)

     display_discordance=[]
     for i in range((no_alternatives)+1):
         display_discordance.append([])
         for j in range((no_alternatives)+1):
             if((i==0)&(j==0)):
                 display_discordance[i].append("*")

             elif((i==0)&(j!=0)):
                 display_discordance[i].append(alternatives[j-1])

             elif((i!=0)&(j==0)):
                 display_discordance[i].append(alternatives[i-1])

             else:
                 display_discordance[i].append(discordance_set[i-1][j-1])

     print(tabulate(display_discordance,tablefmt="grid"))



############################################################   AGGREGATE DOMINANCE MATRIX  #################################################################################################





     #aggregate the concordance and dicordance set
     final_set=[]
     for i in range(no_alternatives):
         final_set.append([])
         for j in range(no_alternatives):
    
             final_set[i].append(discordance_set[i][j] and concordance_set[i][j])   
        
     #print("final set values are obtained")  
     #for i in final_set:
     #   print(i)




     #To display aggregate matrix in table format
     display_aggregate=[]
     for i in range((no_alternatives)+1):
         display_aggregate.append([])
         for j in range((no_alternatives)+1):
             if((i==0)&(j==0)):
                 display_aggregate[i].append("*")

             elif((i==0)&(j!=0)):
                 display_aggregate[i].append(alternatives[j-1])

             elif((i!=0)&(j==0)):
                 display_aggregate[i].append(alternatives[i-1])

             else:
                 display_aggregate[i].append(final_set[i-1][j-1])

     print("Aggregate Dominance matrix")
     print(tabulate(display_aggregate,tablefmt="grid"))

     row=len(display_aggregate)
     print("Rows in Aggregat Dominance matrix=",row)
     column=len(display_aggregate[0])
     print("Columns in Aggregate Dominance matrix=",column)


####################################################################     RANKING ESTIMATION      ############################################################################################    
     print("THE PARTIAL RANKS PRODUCED ARE AS FOLLOWS")
     for i in range(row):
          for j in range(column):
              if(display_aggregate[i][j]==1):
                   print(display_aggregate[i][0] ,"> ",display_aggregate[0][j])

    
        
     
    
     


     



  


     
my_btn=Button(root,text="Select a file",command=openfunc).pack()


root.mainloop()

