# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:10:49 2018

@author: Ben.Olson
"""

import csv

filename = input("What is the name of your file? ")
beginner_lessons = [("Beginner: 1. J, F, and Space", 11),
                    ("Beginner: 2. U, R, and K Keys", 14),
                    ("Beginner: 3. D, E, and I Keys", 11),
                    ("Beginner: 4. C, G, and N Keys", 12),
                    ("Beginner: 5. Beginner Review 1", 10),
                    ("Beginner: 6. T, S, and L Keys", 12),
                    ("Beginner: 7. O, B, and A Keys", 13),
                    ("Beginner: 8. V, H, and M Keys", 13),
                    ("Beginner: 9. Period and Comma", 11),
                    ("Beginner: 10. Beginner Review 2", 10),
                    ("Beginner: 11. W, X, and ; Keys", 14),
                    ("Beginner: 12. Q, Y, and P Keys", 16),
                    ("Beginner: 13. Z and Enter Keys", 9),
                    ("Beginner: 14. Beginner Wrap-up", 19)]
intermediate_lessons = [("Intermediate: 1. Common English Words", 19),
                        ("Intermediate: 2. Easy Home Row Words", 9),
                        ("Intermediate: 3. Easy Top Row Words", 10),
                        ("Intermediate: 4. Easy Bottom Row Words", 7),
                        ("Intermediate: 5. Shift Key and Capitalization", 8),
                        ("Intermediate: 6. Sentences", 15),
                        ("Intermediate: 7. Speed Drills", 10),
                        ("Intermediate: 8. Basic Punctuation", 10),
                        ("Intermediate: 9. Paragraphs", 7),
                        ("Intermediate: 10. Advanced Punctuation", 8),
                        ("Intermediate: 11. Intermediate Wrap-up", 10)]
advanced_lessons = [("Advanced: 1. Skill Builder Drills", 13),
                    ("Advanced: 2. Numbers Letters Numbers", 16),
                    ("Advanced: 3. Jokes and Laughs", 29),
                    ("Advanced: 4. Accuracy Drills", 20),
                    ("Advanced: 5. Nitro Type Content", 13),
                    #("Advanced: 6. Advanced Symbols", 7),
                    #("Advanced: 7. Numeric Keypad", 20),
                    #("Advanced: 8. Common Medical Terms", 17),
                    ("Advanced: 9. Advanced Wrap-up", 26)]

lesson_group_1 = beginner_lessons[0:5]
lesson_group_2 = intermediate_lessons[0:10]
lesson_group_3 = advanced_lessons[0:5]

quiz_1 = beginner_lessons[5]
quiz_2 = intermediate_lessons[10]
quiz_3 = advanced_lessons[5]

with open(filename, newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
     
    for r in [r for row in reader if row[4] in lessons_group_1]:
        print(r)
        
        