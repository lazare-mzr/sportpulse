# sportpulse ეს არის სპორტული პლატფორმა, რომელიც აერთიანებს UFC-ს, Formula 1-სა და ფეხბურთს. მომხმარებლებს საშუალება აქვთ ნახონ მომდევნო ბრძოლები, რბოლები და მატჩები, ასევე მიიღონ ამომწურავი ინფორმაცია მიმდინარე და მომავალი სპორტული მოვლენების შესახებ. საიტი უზრუნველყოფს სწრაფ და განახლებად წვდომას პოპულარული სპორტების სამყაროზე.

ფუნქციონალები:

მომხმარებლის ავტორიზაცია და რეგისტრაცია
(პაროლის დაშიფვრა generate_password_hash-ით, შემოწმება check_password_hash-ით)

მომხმარებლის სესიის მართვა
(session, login_required სტილის ფუნქცია @wraps და abort ქმედებები)

მონაცემთა ბაზასთან კავშირი და მისი მართვა
(SQLite ან SQLAlchemy მოდულით მონაცემების შენახვა და წამოღება)

გვერდების დინამიკური გენერაცია და გადამისამართება
(render_template, redirect, url_for, request)

შეტყობინებების ჩვენება
(flash – მაგალითად, შეცდომების ან წარმატების მესიჯებისთვის)

HTML და CSS დიზაინი
(მომხმარებლისთვის ვიზუალური ინტერფეისის შექმნა და სტილიზაცია)

