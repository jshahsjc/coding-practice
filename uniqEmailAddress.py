"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?



Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
"""

"""
Create an empty list (we'll return this as final result)
create an empty dictionary,
key will be domain and value will be a list of local names
for a given email from the list:
split with @, save first index as key and second as value, in a dictinary.

Iterate through values (lists) of dictionary:
   for each list element in a list,
      1. check if it has '+', if so, remove rest of the string
      2. check if it has '.', if so, split('.') and "".join()
   After this processing, convert lists to a sets to remove duplicates
   Append to the final result list:
      Iterate through key, values in dictionary:
         for each value in values,
            final list.append(value + "@" + key)
   return len(final list)
"""

class Solution(object):
   def numUniqueEmails(self, emails):
      """
      :type emails: List[str]
      :rtype: int
      """
      final_res = []
      email_dict = {}

      for email in emails:
         local_user = email.split('@')[0]
         domain = email.split('@')[1]
         if domain in email_dict:
            email_dict[domain].append(local_user)
         else:
            email_dict[domain] = [local_user]
         print str(email_dict)

      for domain, user_list in email_dict.items():
         for username in user_list:
            temp = ''
            if '+' in username:
               temp += username.split('+')[0]
            if '.' in temp:
               temp1 = temp.split('.')
               temp = "".join(temp1)

            final_res.append(temp + '@' + domain)
            print final_res

      return len(set(final_res))


I1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

s = Solution()
print "Number of uniqe emails sent: " + str(s.numUniqueEmails(I1))
