# RedSnakes

  # App Description
  
  Our aim was to create a Conference Management System capable of automatically managing the information related to scientific conferences and their organisation. 
  
  Firstly, the client desired the application to be capable of supporting multiple types of users, such as: 
    <ul><li>Listeners, that attend conferences </li>
    <li>Speakers, that register papers that will later on be presented in said conferences. Those mentioned papers may eventually be published</li>
    <li>Chair members, that organize, as well as manage the conferences and review and suggest improvements to the papers. Chair members can also belong to the following committees (Program Committee member, that manage one conference and its sections, and choose which papers will be presented in each of the sections, Steering Committee member, that decides on the dates and locations of future conferences) </li>
  </ul>

  Secondly, specific functionalities and privileges should be accessible depending on the type of the authenticated user (for example, only speakers should be able to upload, or only chair members should be able to review submitted papers).
  Finally, the application should be able to facilitate and optimize the organisation of conferences and the UX should be friendly and easy to use.
  
  
  # Technologies used
  Description of technologies used: programming language, ORM, diagrams, version control, UI prototyping, testing etc.
  
     We opted for Python as the programming language of the application, together with the Django web framework for the backend side, using an SQLite database layer. 

     For the frontend technologies, we chose to use HTML, CSS6, Javascript, together with jQuery and Bootstrap. 

     We decided on Django ORM for interactions with our databases, because of its great integration with the rest of the tools we used.

     Concerning the diagrams, we used a multitude of tools, however the vast majority of them were created using the draw.io online diagram tool.

     Regarding version control, we decided to use Git, because most of us were already familiar with it, and used GitHub to host our code repository.

     We used Photoshop together with MS Paint in order to obtain a prototype for our UX. Following this approach, we settled on the aspect of each page of our web application.

     For the testing phase of the application, we used manual testing in Python, coupled with blackbox automatic testing using the Django Simpletest framework.
