# CDW_Watson

This is the project site for the CDW Nao robot demo.  Here is an overview of the files that are on this site.

1) Flow Chart for Personality Inisight Demo.doc: Provides overview of demo flow, and current progress towards completing steps.
2) Flow Chart for Visual Recognition Demo.doc: Provides overview of demo flow, and current progress towards completing steps.
3) Flow Chart for Tweet Demo.doc: Provides overview of demo flow, and current progress towards completing steps.
4) visual_recognition.py: Sample Python code that works with the IBM Bluemix visual recognition service.  You must add the authorization information into the code for the service in order for it to function.  This code will is intended to be incorporated into a Choregraphe file for the robot behavior.
5) personality_insights.py: Sample Python code that works with the IBM Bluemix personality insights service.  You must add the authorization information into the code for the service in order for it to function.  ** It also requires the 'profile.json' file be in the same direcotry. ** This code will is intended to be incorporated into a Choregraphe file for the robot behavior.
6) profile.json: Contains twitter data that the 'personality_insights.py' file uses to run the services against.  
