import pandas as pd


class Students:
    def __init__(self):

        self.df_under_grd = pd.read_csv('und_grd.csv', index_col=False)  # Having the old Students datas
        self.df_post_grd = pd.read_csv('post_grd.csv', index_col=False)

    @property
    def add(self) :
        user = ""
        while user !='exit':
            user = input('Choose the status 0 for "Undergradute", 1 for "Postgradute": ')
            if user == "0":
                std_id = input('Please enter std_id: ')
                if std_id == "":
                    std_id = input("you are entering nothing, please tap 'Enter' if NG :) ")

                full_name = input('Please enter full_name: ')
                if full_name == "":
                    full_name = input("you are entering nothing, please tap 'Enter' if NG :) ")

                nation = input('Please enter natioanality: ')
                if nation == "":
                    nation = input("you are entering nothing, please tap 'Enter' if NG :) ")

                gender = input('Please enter gender: ')
                if gender == "":
                    gender = input("you are entering nothing, please tap 'Enter' if NG :) ")

                fac = input('Please enter faculty: ')
                if fac == "":
                    fac = input("you are entering nothing, please tap 'Enter' if NG :) ")

                ad_year = input('Please enter admission_year: ')
                if ad_year == "":
                    ad_year = input("you are entering nothing, please tap 'Enter' if NG :) ")

                res_hall= input('Please enter res hall: ')
                if res_hall == "":
                    res_hall = input("you are entering nothing, please tap 'Enter' if NG :) ")

                new_row_und = pd.Series(data={"Student ID": std_id, "Full Name":full_name, "Nationality":nation,  # created temporarily pandas Series 
                                        "Gender":gender, "Admission year":ad_year, "Faculty":fac,
                                         "Res Hall" : res_hall})
                self.df_under_grd = self.df_under_grd.append(new_row_und, ignore_index=True)  # Concatineting actual Dataframe and Series

            elif user == "1":
                std_id = input('Please enter std_id: ')
                if std_id == "":
                    std_id = input("you are entering nothing, please tap 'Enter' if NG :) ")

                full_name = input('Please enter full_name: ')
                if full_name == "":
                    full_name = input("you are entering nothing, please tap 'Enter' if NG :) ")

                nation = input('Please enter natioanality: ')
                if nation == "":
                    nation = input("you are entering nothing, please tap 'Enter' if NG :) ")

                gender = input('Please enter gender (Please Enter "M" for Male, "F" for Female): ')
                if gender == "":
                    gender = input("you are entering nothing, please tap 'Enter' if NG :) ")

                fac = input('Please enter faculty: ')
                if fac == "":
                    fac = input("you are entering nothing, please tap 'Enter' if NG :) ")

                ad_year = input('Please enter admission_year: ')
                if ad_year == "":
                    ad_year = input("you are entering nothing, please tap 'Enter' if NG :) ")

                res_topic= input('Please enter research topic: ')
                if res_topic == "":
                    res_topic = input("you are entering nothing, please tap 'Enter' if NG :) ")

                super_name= input('Please enter Supervisor Name: ')
                if super_name == "":
                    super_name = input("you are entering nothing, please tap 'Enter' if NG :) ")

                new_row_post = pd.Series(data={"Student ID": std_id, "Full Name": full_name, "Nationality": nation, 
                                        "Gender": gender,"Admission year" : ad_year, "Faculty" :fac, 
                                        "Supervisor name": super_name, "Research topic": res_topic}, index=None)
                self.df_post_grd = self.df_post_grd.append(new_row_post, ignore_index=True)

            elif user != 'exit':
                print("Please Enter correct option, 'exit' to exit")

        self.df_under_grd.to_csv('und_grd.csv', index=False)  # to save the UnderGraduate students as csv
        self.df_post_grd.to_csv('post_grd.csv', index=False)  # to save the PostGraduate students as csv

    def remove(self, std_id):
        
        self.std_id = std_id

        if self.std_id in self.df_under_grd['Student ID'].values:
            name = self.df_under_grd[self.df_under_grd['Student ID'] ==  self.std_id]  # to know the removed student Full Name
            self.df_under_grd = self.df_under_grd.drop(self.df_under_grd[self.df_under_grd == self.std_id].index)
            print(f"{name['Full Name'][0][0]} is successfullly removed!")

        elif self.std_id in self.df_post_grd['Student ID'].values:
            name = self.df_post_grd[self.df_post_grd['Student ID']==  self.std_id]
            self.df_post_grd = self.df_post_grd.drop(self.df_post_grd[self.df_post_grd == self.std_id].index)
            print(f"{name['Full Name'][0][0]} is successfullly removed!")

        else:
            print('this ID is Not Found!')

        self.df_under_grd.to_csv('und_grd.csv', index=False) 
        self.df_post_grd.to_csv('post_grd.csv', index=False) 

    def find(self, std_id):
        self.df = pd.concat([self.df_under_grd, self.df_post_grd], keys=['UnderGraduate', 'PostGraduate'])

        self.std_id = std_id
        return self.df.loc[self.df['Student ID'] == self.std_id]
    
    @property
    def display_all(self):

        self.df = pd.concat([self.df_under_grd, self.df_post_grd], keys=['UnderGraduate', 'PostGraduate'])

        return self.df

stud = Students()
# stud.add
# print(stud.display_all)
stud.remove(std_id='d')
print(stud.find(std_id='w'))