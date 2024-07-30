# Start-GPT Email Plugin: Revolutionize Your Email Management with Start-GPT 🚀

The Start-GPT Email Plugin is an innovative and powerful plugin for the groundbreaking base software, Start-GPT. Harnessing the capabilities of the latest Start-GPT architecture, Start-GPT aims to autonomously achieve any goal you set, pushing the boundaries of what is possible with artificial intelligence. This email plugin takes Start-GPT to the next level by enabling it to send and read emails, opening up a world of exciting use cases.

[![Twitter Follow](https://img.shields.io/twitter/follow/riensen?style=social)](https://twitter.com/riensen)
[![GitHub Repo stars](https://img.shields.io/github/stars/khulnasoft/start-gpt-plugins?style=social)](https://github.com/khulnasoft/Start-GPT-Plugins/stargazers)

<img width="1063" alt="start-gpt-email-plugin" src="https://user-images.githubusercontent.com/3340218/233331404-fd663c98-5065-4aa5-8cfb-12ce3ed261d0.png">

<img width="1011" alt="gmail-view-start-gpt-email-plugin" src="https://user-images.githubusercontent.com/3340218/233331422-c5afe433-d4ad-48e0-a0e4-2783cc5f842b.png">

## 🌟 Key Features

- 📬 **Read Emails:** Effortlessly manage your inbox with Start-GPT's email reading capabilities, ensuring you never miss important information.
- 📤 **Auto-Compose and Send Emails**: Start-GPT crafts personalized, context-aware emails using its advanced language model capabilities, saving you time and effort.
- 📝 **Save Emails to Drafts Folder:** Gain more control by letting Start-GPT create email drafts that you can review and edit before sending, ensuring your messages are fine-tuned to your preferences.
- 📎 **Send Emails with Attachments:** Effortlessly send emails with attachments, making your communication richer and more comprehensive.
- 🛡️ **Custom Email Signature:** Personalize your emails with a custom Start-GPT signature, adding a touch of automation to every message sent by Start-GPT.
- 🎯 **Auto-Reply and Answer Questions:** Streamline your email responses by letting Start-GPT intelligently read, analyze, and reply to incoming messages with accurate answers.
- 🔌 **Seamless Integration with Start-GPT:** Enjoy easy setup and integration with the base Start-GPT software, opening up a world of powerful automation possibilities.

Unlock the full potential of your email management with the Start-GPT Email Plugin and revolutionize your email experience today! 🚀

## 🔧 Installation

Follow these steps to configure the Start-GPT Email Plugin:

### 1. Follow Start-GPT-Plugins Installation Instructions
Follow the instructions as per the [Start-GPT-Plugins/README.md](https://github.com/khulnasoft/Start-GPT-Plugins/blob/master/README.md)

### 2. Locate the `.env.template` file
Find the file named `.env.template` in the main `/Start-GPT` folder.

### 3. Create and rename a copy of the file
Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Start-GPT` folder.

### 4. Edit the `.env` file
Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

### 5. Add email configuration settings
Append the following configuration settings to the end of the file:

```ini
################################################################################
### EMAIL (SMTP / IMAP)
################################################################################

EMAIL_ADDRESS=
EMAIL_PASSWORD=
EMAIL_SMTP_HOST=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_IMAP_SERVER=imap.gmail.com

# Optional Settings
EMAIL_MARK_AS_SEEN=False
EMAIL_SIGNATURE="This was sent by Start-GPT"
EMAIL_DRAFT_MODE_WITH_FOLDER=[Gmail]/Drafts
```

1. **Email address and password:**
    - Set `EMAIL_ADDRESS` to your sender email address.
    - Set `EMAIL_PASSWORD` to your password. For Gmail, use an [App Password](https://myaccount.google.com/apppasswords).

2. **Provider-specific settings:**
    - If not using Gmail, adjust `EMAIL_SMTP_HOST`, `EMAIL_IMAP_SERVER`, and `EMAIL_SMTP_PORT` according to your email provider's settings.

3. **Optional settings:**
    - `EMAIL_MARK_AS_SEEN`: By default, processed emails are not marked as `SEEN`. Set to `True` to change this.
    - `EMAIL_SIGNATURE`: By default, no email signature is included. Configure this parameter to add a custom signature to each message sent by Start-GPT.
    - `EMAIL_DRAFT_MODE_WITH_FOLDER`: Prevents emails from being sent and instead stores them as drafts in the specified IMAP folder. `[Gmail]/Drafts` is the default drafts folder for Gmail.


### 6. Allowlist Plugin
In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################

#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=StartGPTEmailPlugin
```

## 🧪 Test the Start-GPT Email Plugin

Experience the plugin's capabilities by testing it for sending and receiving emails.

### 📤 Test Sending Emails

1. **Configure Start-GPT:**
   Set up Start-GPT with the following parameters:
   - Name: `CommunicatorGPT`
   - Role: `Communicate`
   - Goals:
     1. Goal 1: `Send an email to my-email-plugin-test@trash-mail.com to introduce yourself`
     2. Goal 2: `Terminate`

2. **Run Start-GPT:**
   Launch Start-GPT, which should use the email plugin to send an email to my-email-plugin-test@trash-mail.com.

3. **Verify the email:**
   Check your outbox to confirm that the email was sent. Visit [trash-mail.com](https://www.trash-mail.com/) and enter your chosen email to ensure the email was received.

4. **Sample email content:**
   Start-GPT might send the following email:
   ```
   Hello,

   My name is CommunicatorGPT, and I am an LLM. I am writing to introduce myself and to let you know that I will be terminating shortly. Thank you for your time.

   Best regards,
   CommunicatorGPT
   ```

### 📬 Test Receiving Emails and Replying Back

1. **Send a test email:**
   Compose an email with a simple question from a [trash-mail.com](https://www.trash-mail.com/) email address to your configured `EMAIL_ADDRESS` in your `.env` file.

2. **Configure Start-GPT:**
   Set up Start-GPT with the following parameters:
   - Name: `CommunicatorGPT`
   - Role: `Communicate`
   - Goals:
     1. Goal 1: `Read my latest emails`
     2. Goal 2: `Send back an email with an answer`
     3. Goal 3: `Terminate`

3. **Run Start-GPT:**
   Launch Start-GPT, which should automatically reply to the email with an answer.

### 🎁 Test Sending Emails with Attachment

1. **Send a test email:**
   Compose an email with a simple question from a [trash-mail.com](https://www.trash-mail.com/) email address to your configured `EMAIL_ADDRESS` in your `.env` file.

2. **Place attachment in Start-GPT workspace folder**
   Insert the attachment intended for sending into the Start-GPT workspace folder, typically named start_gpt_workspace, which is located within the cloned [Start-GPT](https://github.com/khulnasoft/Start-GPT) Github repository.

3. **Configure Start-GPT:**
   Set up Start-GPT with the following parameters:
   - Name: `CommunicatorGPT`
   - Role: `Communicate`
   - Goals:
     1. Goal 1: `Read my latest emails`
     2. Goal 2: `Send back an email with an answer and always attach happy.png`
     3. Goal 3: `Terminate`

4. **Run Start-GPT:**
   Launch Start-GPT, which should automatically reply to the email with an answer and the attached file.
