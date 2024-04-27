from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def test_accuracy_with_stats(spam_or_ham_values_actual, spam_or_ham_values_calc):
  print("ACCURACY: ", accuracy_score(spam_or_ham_values_actual, spam_or_ham_values_calc))
  print("STATS: ", classification_report(spam_or_ham_values_actual, spam_or_ham_values_calc))
  print("CONFUSION MATRIX: ", confusion_matrix(spam_or_ham_values_actual, spam_or_ham_values_calc))

def calculate_accuracy(calc, actual, test_email_count):
  total_spam_calc = 0
  total_spam_actual = 0
  for i in range (test_email_count):
    if calc[i] == 1:
      total_spam_calc += 1
    if actual[i] == 1:
      total_spam_actual += 1
  spam_calc_p = total_spam_calc/test_email_count
  spam_actual_p = total_spam_actual/test_email_count
  print("Calculated", spam_calc_p*100, "%")
  print("Actual", spam_actual_p*100, "%")