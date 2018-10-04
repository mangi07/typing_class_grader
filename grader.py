# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:10:49 2018

@author: Ben.Olson
"""

import csv

filename = input("What is the name of your file? ")

# tuple: lesson description, number of screens, grouping for grading purposes
lessons = {"Beginner: 1. J, F, and Space": [11, 0],
           "Beginner: 2. U, R, and K Keys": [14, 0],
           "Beginner: 3. D, E, and I Keys": [11, 0],
           "Beginner: 4. C, G, and N Keys": [12, 0],
           
           "Beginner: 5. Beginner Review 1": [10, 1],
           
           "Beginner: 6. T, S, and L Keys": [12, 2],
           "Beginner: 7. O, B, and A Keys": [13, 2],
           "Beginner: 8. V, H, and M Keys": [13, 2],
           "Beginner: 9. Period and Comma": [11, 2],
            
           "Beginner: 10. Beginner Review 2": [10, 3],
           
           "Beginner: 11. W, X, and ; Keys": [14, 4],
           "Beginner: 12. Q, Y, and P Keys": [16, 4],
           "Beginner: 13. Z and Enter Keys": [9, 4],
            
           "Beginner: 14. Beginner Wrap-up": [19, 5],

           "Intermediate: 1. Common English Words": [19, 6],
           "Intermediate: 2. Easy Home Row Words": [9, 6],
           "Intermediate: 3. Easy Top Row Words": [10, 6],
           "Intermediate: 4. Easy Bottom Row Words": [7, 6],
            
           "Intermediate: 5. Shift Key and Capitalization": [8, 7],
           "Intermediate: 6. Sentences": [15, 7],
           "Intermediate: 7. Speed Drills": [10, 7],
           
           "Intermediate: 8. Basic Punctuation": [10, 8],
           "Intermediate: 9. Paragraphs": [7, 8],
           "Intermediate: 10. Advanced Punctuation": [8, 8],
           
           "Intermediate: 11. Intermediate Wrap-up": [10, 9],

           "Advanced: 1. Skill Builder Drills": [13, 10],
           "Advanced: 2. Numbers Letters Numbers": [16, 10],
           "Advanced: 3. Jokes and Laughs": [29, 10],
           "Advanced: 4. Accuracy Drills": [20, 10],
           "Advanced: 5. Nitro Type Content": [13, 10],
          #"Advanced: 6. Advanced Symbols": [7, 8],
          #"Advanced: 7. Numeric Keypad": [20, 8],
          #"Advanced: 8. Common Medical Terms": [17, 8],
           "Advanced: 9. Advanced Wrap-up": [26, 11]}

benchmark = 30 # wmp

students = {}


with open(filename, newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    
    
    for row in reader:
        username = row[0]
        currlesson = row[4]
        screenstyped = int(row[5])
        wpm = int(row[8])
        accuracy = float(row[9].strip('%'))/100
        
        if not username in students:
            students[username] = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
        
        try:
            totalscreens = lessons[currlesson][0]
            groupnumber = lessons[currlesson][1]
        except KeyError:
            if currlesson in lessons:
                students[username][groupnumber].append(
                        {"lesson":currlesson, "grade":0})
            continue
        
        grade = min(1, ((wpm/benchmark) + accuracy)/2 * (screenstyped/totalscreens))
        students[username][groupnumber].append({"lesson":currlesson, "grade":grade})

print("number of students graded: ", len(students))

groupnumbers = [0,1,2,3]

for student,records in students.items():
    print("\n*****")
    print(student)
    for k,v in records.items():
        if k in groupnumbers and len(v)>0:
            print("\nGROUP ", k, ":")
            count = 0
            _sum = 0
            for less in v:
                _sum += less['grade']
                count += 1
                print("lesson: ", less['lesson'], "\tgrade: ", less['grade'])
            avg = _sum/count
            print("GROUP AVERAGE:\t", avg)
    print("\n")

    