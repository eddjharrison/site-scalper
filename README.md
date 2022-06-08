# site-scalper
Simple string scalper for websites with automated Gmail-email alerts upon a true return.

Example code:

```
from site_scalper import main

main.run(45, "https://www.passport.service.gov.uk/urgent/?",
        subject="Passport appointment found!", 
        sender="johnapplseed@autoscalper.net",
        hit_str1="Start an application", 
        hit_str2=""To apply online you'll need",
        mail_text="PASSPORTS APPOINTMENTS AVAILABLE",
        neg_str=Sorry, there are no available appointments,
        recipients=["happyBrit@bojo.nhs", "votestay@dontleave.eu")
```

