## Grade Summary (Group): 

- Quality of Planning Document: 88
- Quality of Requirements (in Kanban): 93

Combined Grade: 91

## Planning Document Feedback (Group): 

- You have a good start on your system description, but it still needs a little work. It would be even better if you could state this in a way that makes the value of your system very clear to people not familiar with lesion detection. Ultimately, you would like to take this system description and use it for your Rhodes Symposium abstract. The closer we can get it to the final form now the easier it will be later.
- Between the basic overview and your design description, you have painted a clear picture of how the system will be used. My only suggestion is that the 'major system components' should all be listed in the system diagram. Right now the two seem distinct. But the purpose of the system diagram is to show how the major system components interact. Somehow we need to connect the dots between the list of components and their interactions (as shown in the system diagram).
- Your epics are great. My only request is that you have a title or label for each epic. You have this on your Trello board, but not in your planning document.
- Your non- functional requirements are reasonable, but I am wondering why you want to restrict the file size to 1 MB or less. I would have expected a non- functional requirement in the opposite direction; for example, program must be able to support file sizes up to 1 MB. The way its worded now, it sounds like you want the program to generate an error if the file size is greater than 1 MB. Is that correct or am I interpreting it incorrectly. You way also want to expand the 'double click to launch the program' into a more general usability requirement. For example, 'the system should be intuitive and easy to use'. The double click to launch could then be made a functional requirement (i.e., user story) that helps with that non- functional requirement of usability.
- The list of technologies look reasonable, but I don't understand where you are using Postgres. Did you mean to remove that after changing your design to use the file system exclusively?
- I'd like to discuss your MVP a little more. It would help if there was a paragraph that better described the user experience (provided interface) given this minimal set of features. Would it basically be selecting data from the file system, running a previously trained model in the background for 10 minutes, and then writing the output of the model back to the file system? No preprocessing? No visualization? Does this MVP improve on Stu's current process?
- Your roadmap is a little unclear. For example, what does 'finalize app development program' mean? I'm guessing you mean just getting anything running in QT, but it would be better if you target a specific feature. Later you have 'implement front- end components', but what does that mean? Clearly the visualization dashboard is a front- end component, but it happens in the next sprint. Your roadmap would be much better if you can list the specific features that are being targetted for each sprint (loading/accessing data, selecting and running saved models, training new models, visualizing model output without occlusion, etc.)
- Your roadmap should also state when you expect your MVP to be achieved.

## Requirements Feedback (Group): 

- Generally great user stories! Well written and easy to understand the value of most of your user stories.
- Your stories have clear, consistently formatted titles.
- All stories are traceable to epics, which is great.
- Most of your stories have acceptance criteria, which is also great. 
- In a few cases, the details on how to verify the user story are a little unclear for the ACs. For example, how would someone test that the data had been selected properly for US1? Not sure what 'Drop point for .csv file with 2- d array of legion data' means in terms of testing.
- I don't see any estimates on the level of effort for your stories. I think adding these would help you better plan your sprints and the division of labor within your group.
- It looks like you prioritized your work based on epics, which is fine. It is a little hard for me to directly connect these epics to your roadmap, but you can refine this as you go.
- Overall, good job!
