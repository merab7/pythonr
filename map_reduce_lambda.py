import statistics

# map ახორციელებს კონკრეტული ლოგიკას იტერირებადზე(ლისტი, ტუპლ, სეტი) ყოველ ობიექქტზე და გვაძლევს მაპ ობჯექტს რომელიც ლისტ კონსტრუქტორით შეიძლება იქცეს ახალ ლისტად
l_in_c = [
    ("berlin", 29),
    ("cairo", 36),
    ("buenos aires", 19),
    ("los angeles", 26),
    ("Tokyo", 27),
    ("new york", 28),
    ("london", 22),
    ("beijing", 32),
]
l_in_f = list(map(lambda x: (x[0], 9 / 5 * x[1] + 32), l_in_c))


# filter ეს ფუნქცია მოცემულ ლოგიკას არ დაქვემდებარებული კომპონენტების გაფდილტვრას ახდენს და გვიბრუნებს ობჯექთის სახით მაგ:
data = [1.3, 2.5, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

more_then_avg = list(filter(lambda x: x > avg, data))
print(more_then_avg)

countries = ["", "germany", "georgia", "usa", "", "austria", ""]
removed_nissing_data = list(filter(None, countries))
# sort and sorted სორთი არის მეთოდი რომელიც არსებული კომპონენტის (ლისტი, სეტი) დასორტვას ახდენს აქვს reverse და key  პარამეტრები
# key პარამეტრში შერიძლება გაიწეროს ლოგიკა რომლის მიხედვითაც მხოდება დასორთვა. აღსანიშნავია ფაქტი რომ
# სორთი უშუალოდ ცვლის არსებულ კომპონენტს შესაბამისად ვერ მოხდება არამუტირებადი კომპონენეტების როგორიცაა ტუპლს დასორთვა ამ მეთოდით. data.sort()
# რას შეეხება sorted(data) ამ შემთხვევაში sorted()ის გააცნია ყველ ის პარამეტრი რაც sort-ს და ამავდროულად ის მოქმედებს არამუტირებად ელემენტებზეც
# ვინაიდან მას გადაყავს ნებისმიერი კომპონეწნტი ლისთში და შემდეგ ახდენს ლოგიკის მათზე განხორციელებას
# ანუ tuples ჯერ იქცევა ლისტად რომელიც უკვე მუტირებადია და შემდეგ დაისორთება და დაგვიბრუნდება ლისტის სახით ხოლო
# ორიგინალი ელემენტი ამ შემთხვევაში tuple უცვლელი რჩება.