def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key] # извлечь запись по ключу, отобразить в форме
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))
def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key] # изменяется существующая запись
    else:
        from person import Person # создать/сохранить новую запись

        record = Book(name='?', age='?') # eval: строки должны
                                            # заключаться в кавычки
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record
