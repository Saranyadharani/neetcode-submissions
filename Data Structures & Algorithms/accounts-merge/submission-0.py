class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px!=py:
            self.parent[px]=py
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_to_id={}  #assigning a unique id to the emails
        emails_to_name={} #assigning the account holder name
        for account in accounts: 
            name=account[0]
            for email in account[1:]:
                if email not in emails_to_id:
                    emails_to_id[email]=len(emails_to_id)
                    emails_to_name[email]=name
        
        # union the emails of same of person
        uf=UnionFind(len(emails_to_id))

        for account in accounts:
            first_email=account[1]
            for email in account[2:]:
                uf.union(emails_to_id[first_email],emails_to_id[email])

        # map the email to the account holder name
        root_to_emails={}
        for email,id in emails_to_id.items():
            root=uf.find(id)
            if root not in root_to_emails:
                root_to_emails[root]=[]
            root_to_emails[root].append(email)

        #display the result
        result=[]
        for root,email in root_to_emails.items():
            name=emails_to_name[email[0]]
            result.append([name]+sorted(email))
        return result                