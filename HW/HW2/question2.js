class Defect {
    constructor(contents) {
        this.bug_id = contents[0];
        this.component = contents[1];
        this.status = contents[2];
        this.resolution = contents[3];
        this.summary = contents[4];
        this.changed = contents[5];
        this.severity = contents[6];
        this.number_comments = contents[7];
        this.os = contents[8];
        this.assignee_id = contents[9];
        this.reporter_id = contents[10];
        this.open_date = contents[11];
        this.closed_date = contents[12];
        this.blocks = []; // (this attribute is an array of ids!)
        this.depends = []; // (this attribute is an array of ids!)
        this.fixed_by_username = contents[13];
        this.fixed_by_real_name = "";
    }
};

// function that reads defects.csv
function readDefects() {
    let objectArray = [];
    let data = fs.readFileSync('defects.csv', 'utf8');
    let rows = data.split('\n');
    var body = rows.slice(1,);
    
    // iterate through all of the lines and turn those into arrays
    // create defect objects from those arrays and put into array of defects
    for (let i = 0; i < body.length; i++) {
        let content = body[i].split(',');
        let currObj = new Defect(content);
        objectArray.push(currObj);
    }
    return objectArray;
}

// reads defect_blocks.csv
function readBlocks(objects) {
    let blocks = fs.readFileSync('defect_blocks.csv', 'utf8');
    let rows = blocks.split('\n');
    var body = rows.slice(1,);

    // iterate through all of the lines, turn those into arrays
    for (let i = 0; i < body.length; i++) {
        let content = body[i].split(',');

        // format which bug blocks the other (from blocks to)
        let from = content[0];
        let to = content[1];
        // push those to an array of blocks for each applicable bug
        let temp = objects.find( (objects) => objects.bug_id == from )
        temp['blocks'].push(to);
    }
    return objects;
}

// reads defect_depends.csv
function readDeps(objects) {
    let deps = fs.readFileSync('defect_depends.csv', 'utf8');
    let rows = deps.split('\n');
    var body = rows.slice(1,);

    // iterate through all of the lines, turn those into arrays
    for (let i = 0; i < body.length; i++) {
        let content = body[i].split(',');
        // format which bug depends on the other (from depends on to)
        let from = content[0];
        let to = content[1];

        // push those to an array of depends for each applicable bug
        let temp = objects.find( (objects) => objects.bug_id == from )
        temp['depends'].push(to);
    }
    return objects;
}

// reads developers.csv
function readDevs(objects) {
    let devs = fs.readFileSync('developers.csv', 'utf8');
    let rows = devs.split('\n');
    var body = rows.slice(1,);

    // iterate through all of the lines, turn those into arrays
    for (let i = 0; i < body.length; i++) {
        let content = body[i].split(',');
        // figure out which is real/which is user
        let real = content[0];
        let user = content[1];

        // change the real name of all applicable developers
        let matchingNames = objects.filter( (objects) => objects.fixed_by_username == user );
        for (let j = 0; j < matchingNames.length; j++) {
            matchingNames[j]['fixed_by_real_name'] = real;
        }
    }

    // change the ones with no real/username mapping to null
    let noNames = objects.filter( (objects) => objects.fixed_by_real_name == '' );
    for (let i = 0; i < noNames.length; i++) {
        noNames[i]['fixed_by_real_name'] = null;
    }

    return objects;
}

function loadObjects() {
    var objectArray = [];
    fs = require('fs');
    // defects.csv
    baseData = readDefects();
    // defect_blocks.csv
    dataWBlocks = readBlocks(baseData);
    // defect_depends.csv
    dataWDeps = readDeps(dataWBlocks);
    // developers.csv
    objectArray = readDevs(dataWDeps);

    return objectArray;
}




function query1(defects){
    // Q3.1: How many defects have been solved by developers 
    // (i.e., status=”RESOLVED” and resolution="FIXED") so far? 
    // Returned value  should be a number
    let resolvedDefects = defects.filter( (objects) => objects.status === 'RESOLVED' )
    let fixed = resolvedDefects.filter( (resolvedDefects) =>  resolvedDefects.resolution === 'FIXED')
    
    return fixed.length;   
}

function query2(defects){
    // Q3.2: Count the number of defects  whose summary attribute include
    // the word "buildbot" regardless of case (ex: “Drone”, and “drone” are treated as the same word).  
    // Returned value  should be a number

    let buildbotCount = defects.filter( (objects) => objects.summary.toLowerCase().search('buildbot') > -1 );
    return buildbotCount.length;  
}

function query3(defects){
    // Q3.3: What percentage of issues are still in the backlog (status!=RESOLVED)? 
    // Returned value  should be a number

    let temp = defects.filter( (objects) => objects.status != 'RESOLVED' )
    // round to 2 decimal places
    return (temp.length*100/defects.length).toFixed(2);
}

function query4(defects){
    // Q3.4: What is the most defective component (that is, the component 
    // that has the highest number of associated defects)? 
    // Returned value  should be a string
    // Notice: Each defect has a component attribute. Here, we count 
    // the number of defects per component. Then, we output the one that has the highest count.
    var compCount = {};

    // get just the components
    let defectMap = defects.map( x => x.component )

    // get the counts for each type of component
    for (let i = 0; i < defectMap.length; i++) {
        if (compCount[defectMap[i]] != undefined) {
            compCount[defectMap[i]] += 1;
        }
        else {
            compCount[defectMap[i]] = 1;
        }
    }
    
    // find which component has the most bugs
    let currMax = 0;
    var maxName;
    for (key in compCount) {
        if (compCount[key] > currMax) {
            currMax = compCount[key];
            maxName = key;
        }
    }
    return maxName;  
}

function query5(defects){
    // Q3.5: What are the usernames of the two developers who mostly fixed 
    // documentation defects (i.e., status === "RESOLVED" && resolution === "FIXED" 
    // && component === "Documentation")? 
    // Returned value  should be an array with two strings ["X" , "Y"]. 
    // X and Y are the two developers (in order) who most fixed documentation defects

    // get the ones with status 'RESOLVED'
    let resolvedDefects = defects.filter( (objects) => objects.status === 'RESOLVED' );
    // of the ones resovled, get those with resolution 'FIXED'
    let fixed = resolvedDefects.filter( (resolvedDefects) =>  resolvedDefects.resolution === 'FIXED');
    // of the ones resolved and fixed, get the usernames of the ones where the component is documentation 
    let docs = fixed.filter( (fixed) => fixed.component === 'Documentation').map( x => x.fixed_by_username);

    var fixCount = {};
    // get a count of all of the fixes made by a distinct username
    for (let i = 0; i < docs.length; i++) {
        if (fixCount[docs[i]] != undefined) {
            fixCount[docs[i]] += 1;
        }
        else {
            fixCount[docs[i]] = 1;
        }
    }

    // calculate the top two usernames that performed the most fixes
    let currMax = 0;
    let secMax = 0;
    var maxName = '';
    var secMaxName = '';
    for (key in fixCount) {
        if (fixCount[key] > currMax) {
            secMax = currMax;
            secMaxName = maxName;
            currMax = fixCount[key];
            maxName = key;
        }
        else if (fixCount[key] > secMax) {
            secMax = fixCount[key];
            secMaxName = key;
        }
    }
    let arr = []
    arr.push(maxName);
    arr.push(secMaxName);
    return arr;   
}

function query6(defects){
    // Q3.6: Is there any circular dependency? (ex:, bug A blocks bug B, 
    // bug B blocks bug C, and bug C blocks bug A) 
    // Returned value  should be a boolean true (i.e., it means that “Yes - 
    // there is a circular dependency in the data”) or false (i.e., it means that 
    // “No - there is not a circular dependency in the data”). For this, rely only on 
    // the defect.blocks values.

    var depDict = {};

    // get the elements that have any dependencies
    let hasDeps = defects.filter( (defects) => defects.depends.length > 0 )
    if (hasDeps == undefined) {
        return false;
    }

    // turn those into an array of [bug_id, [depends]]
    let deps = hasDeps.map( (hasDeps) => [hasDeps.bug_id, hasDeps.depends] )
    if (deps == undefined) {
        return false;
    }

    // turn this data into a dictionary
    for (let i = 0; i < deps.length; i++) {
        depDict[deps[i][0]] = deps[i][1];
    }

    // do bfs starting at each node to see if there are any loops (circular dependency)
    for (key in depDict) {
        if(GraphBFS(depDict, key) == true) {
            return true;
        }
    }

    return false;
}

function GraphBFS(graph, root) {
    var q_frontier = [];
    var visited = new Set();

    q_frontier.push(root);
    while (q_frontier.length > 0) {
        var n = q_frontier[0];
        q_frontier.shift();
        if(visited.has(n)) {
            return true;
        }
        visited.add(n);
        if(graph[n] != undefined) {
            for (let i = 0; i < graph[n].length; i++) {
                q_frontier.push(graph[n][i]);
            }
        }
    }
    return false;
}

let defects = loadObjects();
/*console.log(query1(defects));
console.log(query2(defects));
console.log(query3(defects));
console.log(query4(defects));
console.log(query5(defects));
console.log(query6(defects));*/
query1(defects);
query2(defects);
query3(defects);
query4(defects);
query5(defects);
query6(defects);


