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
1. Download the code from <https://github.com/yaoyaomua/BPMN2ArtifactViewProcess> and <https://github.com/ZhidieWu/ProcessMiningThesis>
2. Open project in IntelliJ IDEA and PyCharm.
3. Download required libraries. (Note: Panda verion must be 1.5.3 or lower version)

### Transformation
1. Input Data logs in PyCharm.
2. Pre-analysing for the data logs.
3. Run main.py get data objects JSON file.
4. Input data objects JSON file and collaboration diagram in IntelliJ IDEA, and run DataObjectTest.


## Related Link
- Projet Github Link: <https://github.com/yaoyaomua/BPMN2ArtifactViewProcess>
<https://github.com/ZhidieWu/ProcessMiningThesis>

- SMATifact Link: <https://link.springer.com/book/10.1007/978-3-030-32412-4>

## About
This project is a part of DTU graduation thesis.
