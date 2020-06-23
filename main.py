from score_management_system import ScoreManagementSystem

if __name__ == "__main__":
    cms = ScoreManagementSystem()
    cms.read('score.csv')
    print(cms.sort("avg","des"))
    cms.write('result.csv',"avg","des")