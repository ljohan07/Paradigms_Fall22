import requests
import csv
import re


HOST="http://129.74.152.125:51053"

def bugs(bug_dict={}):
    with open("total_bugs_per_package.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",", quotechar= '"')
        csv_writer.writerow(["package", "total"])
        
        next_url = f"{HOST}/bugs"
        
        while next_url:
            # makes HTTP GET request
            response = requests.get(next_url)
            # parses the response (.content vs .text vs .json())
            json_resp = response.json()
            #print(json_resp)
            for bug in json_resp["results"]:
                if bug["package"] in bug_dict.keys():
                    bug_dict[bug["package"]] += 1
                else:
                    bug_dict[bug["package"]] = 1
            next_url = json_resp["next"]
        for key in bug_dict.keys():
            csv_writer.writerow([key, bug_dict[key]])


def comments(comment_dict={}):
    with open("total_comments_per_bug.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",", quotechar= '"')
        csv_writer.writerow(["bug_id", "total"])
        
        next_url = f"{HOST}/comments"
        
        while next_url:
            # makes HTTP GET request
            response = requests.get(next_url)
            # parses the response (.content vs .text vs .json())
            json_resp = response.json()
            
            #print(json_resp)
            for comment in json_resp["results"]:
                bug_id = re.search('/bugs/([0-9]*)/', comment["bug"]).group(1)
                if bug_id in comment_dict.keys():
                    comment_dict[bug_id] += 1
                else:
                    comment_dict[bug_id] = 1
            next_url = json_resp["next"]
        for key in comment_dict.keys():
            csv_writer.writerow([key, comment_dict[key]])

def main():    
    bugs()
    comments()


if __name__ == '__main__':
    main()