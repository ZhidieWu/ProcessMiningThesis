# Enrich BPMN Collaboration Diagram with Artifacts

This project provide a prototype for automatically enrich BPMN collaboration diagram with artifacts. This project is a part of configuration for BPM process monitoring platform.

## Installation and Transformation

### Python Environment

1. Python Version: Python 3.9.10 was chosen for the data analysis and machine learning component of this project.
2. Integrated Development Environment (IDE): The Python part of the project was developed in PyCharm.
3. Python Libraries: We utilized the pandas library for data manipulation and analysis, providing data structures and functionality required for manipulating numerical tables and time series data. For machine learning, we used Scikit-learn (sklearn), a powerful library for Python that provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction.

### Java Environment
1. Java Version: The Java component of this project was implemented using Java 17.
2. Integrated Development Environment (IDE): The chosen IDE for the Java part of the project was IntelliJ IDEA.
3. Java Libraries: The project utilizes the Camunda API for manipulating BPMN files.

### Input Conditions
1. The data logs need to contain data from at least one artifact.
2. The data logs need to contain timestamps, process instance numbers, and corresponding activities referring to the BPMN diagram or at least can derive the corresponding activities from other data.
3. The BPMN diagram is well-structured.
4. The BPMN diagrams and the data logs must be consistent.
5. All activities in the data logs must correspond to the activities in the original BPMN diagram. The preceding and following activities must also correspond directly to the preceding and following activities in the source BPMN diagram.

### Installation
1. Download the code from <https://github.com/ZhidieWu/ProcessMiningThesis> and <https://github.com/yaoyaomua/BPMN2ArtifactViewProcess>
2. Open project in IntelliJ IDEA and PyCharm.
3. Download required libraries. (Note: Panda verion must be 1.5.3 or lower version)

### Transformation Steps
PyCharm
1. Download the code from the first link in the above installation (ProcessMiningThesis) and configure the python environment.
2. Input the data log that meet the input conditions in PyCharm. It is recommended that the data log file be placed in the Data folder.
3. Open mian.py to configure the parameters needed for Transformation:  
   [csv_file]: Set the path to the path where the data log was placed in the previous step.  
   [artifact_dict]: Set the value of the dictionary. The key of the dictionary is the name of the artifact. The value of the dictionary is the name of the column in the csv corresponding to the artifact in the key.  
   [selected_artifact]: Select the artifact to be generated for the enriched bpmn collaboration diagram. It should be one of the keys of the artifact_dict.  
   [instanceId]: Select a column in the csv as the process instance.
4. Run main.py get data objects JSON file. The JSON file is in the \Data folder named final_dataobject.json 

Java  

5. Download the code from the second link in the above installation (BPMN2ArtifactViewProcess) and configure the java environment.
6. Input data objects JSON file and collaboration diagram in IntelliJ IDEA. It is recommended to place these two files in the \BPMN2ArtifactViewProcess\models\DataObject folder.  
7. Open \BPMN2ArtifactViewProcess\src\Test\java\StepTest\DataObjectTest.java  
8. run addDataObjectTest() to add the data object with state for BPMN collaboration diagram. The values of the variables in the functions that need to be modified are shown below:  
   [bpmnModelInstance]: Change the path to the path where bpmn is located.  
   [jsonFile]: Change the path to the path where JSON file is located.
   [outputFile]: The output path of the bpmn diagram after adding the data object with states.  
9. run addDataObjectWithoutStateTest() to add the data object without a state for BPMN collaboration diagram. The values of the variables in the functions that need to be modified are shown below:  
   [bpmnModelInstance]: Change the path to the path where bpmn is located.  
   [The parameter in AddDataObjectWithoutState.add()]: Modify the second parameter to selected artifact to be generated for the enriched bpmn collaboration diagram. This value needs to be the same as the selected_artifact parameter in Python.  
   [outputFile]: The output path of the enriched bpmn diagram. 

## Related Link
- Project Github Link: <https://github.com/yaoyaomua/BPMN2ArtifactViewProcess>
<https://github.com/ZhidieWu/ProcessMiningThesis>

- SMATifact Link: <https://link.springer.com/book/10.1007/978-3-030-32412-4>

## About
This project is a part of DTU graduation thesis.
