with open("./bugfix.buggy.shuffled") as buggy:
    records_buggy = [x for x in buggy]
    train_buggy = records_buggy[:148720]
    valid_buggy = records_buggy[148720:167310]
    test_buggy = records_buggy[167310:]
    print(len(train_buggy), len(valid_buggy), len(test_buggy))
with open("./bugfix.fixed.shuffled") as fixed:
    records_fixed = [x for x in fixed]
    train_fixed = records_fixed[:148720]
    valid_fixed = records_fixed[148720:167310]
    test_fixed = records_fixed[167310:]
    print(len(train_fixed), len(valid_fixed), len(test_fixed))

with open('./train.bugfix.buggy', "w") as f:
    for record in train_buggy:
        f.write(record)
with open('./valid.bugfix.buggy', "w") as f:
    for record in valid_buggy:
        f.write(record)
with open('./test.bugfix.buggy', "w") as f:
    for record in test_buggy:
        f.write(record)

with open('./train.bugfix.fixed', "w") as f:
    for record in train_fixed:
        f.write(record)
with open('./valid.bugfix.fixed', "w") as f:
    for record in valid_fixed:
        f.write(record)
with open('./test.bugfix.fixed', "w") as f:
    for record in test_fixed:
        f.write(record)