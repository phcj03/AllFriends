# AllFriends
## 1. Introduction
This manual provides a comprehensive guide to using and understanding AllFriends, a Python-based friend simulating tool that allows you to chat with the best friend, boyfriend, or girlfriend of your dreams. Inspired by the Black Mirror episode "Be Right Back," AllFriends was created with the intention to provide people a perfect virtual companion that can replace a human companion, focusing on monitoring and enhancing the personality of the virtual friend based on the user's input as the conversation between the virtual friend and the human progresses. AllFriends is not meant to eliminate human-to-human relationships but instead meant to serve as an addition or an aid to the user's life, especially if the user has been struggling with loneliness or social anxiety. According to Harvard University, 36% of Americans report “serious loneliness,” so this tool serves to provide a virtaul friend that is not as judgmental as a human or as emotionally rigid as ChatGPT. AllFriends is a work in progress so far, with features tackling personality changes and complex responses still being refined, and new features such as the options for users to create and chat with multiple virtual friends, chat with other users and friends made by other users, submit feedback through a feedback system to further enhance virtual friend personality, gain access to the dialogue between another user and their virtual friend, impersonate another user's virtual friend by sending audios mimicking the virtual friend to that user based on the personality the virtual friend exhibited in their dialogue with their creator and conduct business transactions based on such audios and receive ratings from that user while staying anonymous, engage in group chats, and more coming soon.
## 2. Installation
Before you can use AllFriends, you will need to install Python 3.x. Here are the steps to get started:
1. Clone this repository to your computer: git clone https://github.com/phcj03/AllFriends.git
2. Install the required Python packages: pip install -r requirements.txt
## 3. Getting Started
When you run the program, you will be prompted to choose the type of virtual friend to interact with. You can choose from the following:
1: BestFriend
2: BoyFriend
3: GirlFriend
Simply enter the number corresponding to your desired virtual friend.
## 4. Virtual Friend Customization
After selecting a virtual friend, you have the option to customize their appearance and initial personality. You can choose characteristics for their form, face, accessories, hair, eyes, skin, and personality. Here's how it works:
### 1. Appearance
For each category (e.g., form, face, etc.), you will be presented with a list of characteristics.
Choose one characteristic from each category.
### 2. Initial Personality
You will be presented with a list of characteristics.
You can assign a percentage (multiple of 5) to each characteristic of your choosing to reflect how prominently it appears in your character.
You have a total of 100 percentage points to distribute.
## 5. Interacting with the Virtual Friend
Once you've selected your virtual friend and customized their appearance, you can start interacting with the virtual friend. Here's how it works:
You can enter text-based input to have a conversation with your virtual friend.
The virtual friend can respond to various types of input, including greetings, questions, and statements.
AllFriends has a personality system that can influence the personality of your virtual friend over time based on your interactions and personality by analyzing your sentiment. The system can detect any possible personality change in the virtual friend and make calculations based on the virtual friend's average personality over time, which can result in a notice being triggered asking you to either allow the personality change or not.
## 6. Exiting the Conversation
To exit the conversation, simply type "exit" when prompted for user input. The virtual friend will bid you goodbye, and the conversation will end.
## 7. Security
AllFriends uses Bleach to sanitize HTML by escaping and stripping harmful content.
## 8. Contributing
If you'd like to contribute to AllFriends, please email me at ph2265@nyu.edu.
Contributions and bug reports are welcome.
## 9. License
AllFriends is licensed under the MIT License.
Review the license for more details on usage and distribution.
