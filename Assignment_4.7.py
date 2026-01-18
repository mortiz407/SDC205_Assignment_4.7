#Display studnet ID
print("ManOrt0727")
#Import pandas library 
import pandas as pd
#Import matplotlib for creating graph and charts
import matplotlib.pyplot as plt
#Create a list of 10 students
students = ['Manuel O', 'Steve A', 'Kevin B', 'Mia H', 'Siwar O', 'Ivan R', 'Linda W', 'Carla N', 'Bob H', 'Rene G']
#Create a list of subjects
subjects = ['Math', 'Science']
#Creat a list of grades
class_grade = [[100, 97], [87, 96], [96, 93], [98, 94], [78, 82], [72, 81], [94, 92], [75, 86], [71, 76], [84, 83]]
#Create a MultiIndex using the student names and subjects
#from_product() combines students and subjects to create all possible pairs
#names the index levels as 'Student' and 'Subject'
index = pd.MultiIndex.from_product([students, subjects], names = ['Student','Subject'])
#Flatten the list of grades into a single list using sum()
grade_data = sum(class_grade,[])
#Create a DataFrame with the grade data and the MultiIndex
#the DataFrame will have Student and Subject as index and Grade as column
df = pd.DataFrame({'Grade': grade_data}, index=index)
#groupby('Subject') separates the data by Math and Science
#['Grade'].mean() calculates the average grade for each subject
average = df.groupby('Subject')['Grade'].mean()
print("\nData Frame")
print(average.to_frame().round(2))
#Create a vertical bar chart showing the average grades
#kind='bar' creates a bar chart
#color=['b'] makes the bars blue
average.plot(kind='bar', color=['b'])
#Add a title
plt.title('Average Grades by Subject')
#Label the x-axis 
plt.xlabel('Subject')
#Label the y-axis 
plt.ylabel('Average Grade')
#Display the chart
plt.show()
