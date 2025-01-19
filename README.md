<img src="./pics/anon-comments/anon-comments-header-1000.png" alt="Anon Comments Header" width="400" />

# Anon Comments
Anonymous comments API. Let your user speak without forcing them to login.

This is a simple project done with Python, FastAPI and SQLAlchemy.

It allows anyone visiting your site to leave a comment, optionally providing their username and/or email for more features.

> [!IMPORTANT]
> Implementing such API on a website with a lot of traffic could be dangerous if it isn't properly moderated.
> 
> It's totally OK to implement it on your personal website! Since you will be most likely moderating it yourself at any time.

## Features To-Do List
For the user (your website visitor):
- [ ] **Leave a comment**. No registration needed
- [ ] **Provide a username**. Let others know how to refer to you
- [ ] **Gravatar**. Leave your email to show your Gravatar (email stays private)
- [ ] **Modify/delete a comment**. If you leave your email, you could do that (otherwise contact support)
- [ ] **Get notified about replies**. Works if you leave your email
- [ ] **Report a comment**. See some spam? Simply click the flag button and boom it's gone

For the website owner (you):
- [ ] **Limit requests per IP**. Simpliest anti-DOS technique
- [ ] **Resolve support/report requests**. Leave your email addresses for these purposes. API will message you when a user requested that
- [ ] **Moderate the comments**. Delete suspicious comments, access comments IP addresses, ban IP addresses (could help a little bit)
- [ ] **Get notified about new comments**. Optionally get mails for any comments left on the site. You could group them, e.g. receive a mail only when 5 new comments appeared
