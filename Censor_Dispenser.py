# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#1st Function for emails getting censored base on String paramater
def censor_single_text(email,word):
  censor_email = email_one.replace(word.lower(),'X' * len(word))
  return censor_email

#2nd Function for emails getting censored base on list paramater  
def censor_multi_text(email,words):
  censor_email = email
  for word in words:
    if ((word.lower() in censor_email.lower()) or(word.lower()+"!" in censor_email.lower())):
      orig_match_word_index = censor_email.lower().find(word)
      orig_match_word = censor_email[orig_match_word_index:orig_match_word_index + len(word)]
      censor_email = censor_email.replace(orig_match_word,word.lower())
      censor_email = censor_email.replace(word.lower(),'X' * len(word))
  return censor_email

#3rd Fucntion for emails getting censored based on 2nd function and set of negative words. third parameter was set to all if wanted to censored all the negative words if third parameter is not all then it will skip the first occurence of negative words
def censor_censor_ntext(email,n_words,typ = "ALL"):
  if(typ == "ALL"):
    censor_neg_email = censor_multi_text(email,proprietary_terms)
    censor_mail_part2 = censor_multi_text(censor_neg_email,n_words)
    return censor_mail_part2
  else:
    censor_neg_email = censor_multi_text(email,proprietary_terms)
    censor_neg_email_split = censor_neg_email.split()
    for neg_word in censor_neg_email_split:
      if(neg_word.lower() in n_words):
        exception_n_word = neg_word
        exception_n_word_idx = censor_neg_email.find(exception_n_word)
        break
    censor_mail_part2 = censor_multi_text(censor_neg_email[(exception_n_word_idx + len(exception_n_word)):],n_words)
  return  censor_neg_email[:(exception_n_word_idx + len(exception_n_word))] + censor_mail_part2


#4th function uses 2nd and thir function plus the ability to censor the words before and after the negative /unwanted words
def censor_all(email,neg_words):
  new_email = censor_censor_ntext(email,neg_words)
  new_email_split_paragraph = new_email.split('\n')
  new_email_split_join = []
  new_email_split_full = ''
  for new_email_spt_para in  new_email_split_paragraph:
    new_email_split_word = new_email_spt_para.split()
    for new_email_split_wd in new_email_split_word:
      if ('X' in new_email_split_wd):
        new_email_idx = new_email_split_word.index(new_email_split_wd)
        org_len = len(new_email_split_word[new_email_idx - 1])
        new_email_split_word[new_email_idx - 1] = ('X' * org_len)
        if(new_email_idx != (len(new_email_split_word) -1)):
          org_len = len(new_email_split_word[new_email_idx + 1])
          new_email_split_word[new_email_idx +1] = ('X' * org_len)

    new_email_split_join.append(' '.join(new_email_split_word))
  new_email_split_full = '\n'.join(new_email_split_join)
  return(new_email_split_full)


#Main area to call each functions 
print(censor_all(email_four,negative_words))