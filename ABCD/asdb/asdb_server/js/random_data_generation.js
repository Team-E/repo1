/**
 * Created by hiroshi on 05/12/15.
 */



//Legend titles

window.onload = function(){

    w = 500;
    h = 500;

    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    colorscale = d3.scale.category10();


    //following is data...

    methods_list = ['LSD','Mushroom','Yoga','Music','Meditation','Dimenhydrinate','peyote','coffee','tabacco'];

    question1 = {"name":"5D ASC","explanation":"This is famous questions when you assess the altered state where brains are ","factor":["Elementary visual alternations","Disembodiment","Impaired control & cognition",
        "Anxiety","Blissful state","experience of unity","Religious experience","Insightfulness","Changed meaning of percepts",
        "Vivid imagery","Audio-visual synesthaesia"]};

    question2 = {"name":"PCI","explanation":"this is most well-known index","factor":["Delusion","Disorganization","Hallucination","Excitement","Grandiosity","Persecution"
        ,"Hostility","Unusual thought content"]};

    question3 = {"name":"HRS","explanation":"this is quite widely used in some specific kind of paper","factor":["Elementary visual alternations","Disembodiment","Impaired control & cognition",
        "Anxiety","Blissful state","experience of unity","Religious experience","Insightfulness","Changed meaning of percepts",
        "Vivid imagery"]};

    question4 = {"name":"ARCI","explanation":"this is nice","factor":["Elementary visual alternations","Disembodiment","Impaired control & cognition",
        "Anxiety","Blissful state","Changed meaning of percepts",
        "Vivid imagery","Audio-visual synesthaesia"]};


    title_list = [question1.name,question2.name,question3.name,question4.name];
    explanations_list = [question1.explanation,question2.explanation,question3.explanation,question4.explanation];
    question_list = [question1.factor,question2.factor,question3.factor,question4.factor];

    table_body = document.getElementById("table_body");


    for(var i=0;i<methods_list.length;i++){

        tr = document.createElement('tr');
        a_method = '<td><a href="">' + methods_list[i] + '</a></td><td>explanation</td>';

        for(var j=0;j<4;j++){
            temp = "";
            temp += '<td><div class="checkbox"><label><input type=radio value=second_im name=';
            temp += methods_list[i];
            temp += '></label></div></td>';
            a_method += temp;
        }

        tr.innerHTML = a_method;
        table_body.appendChild(tr);

    }

    methods_value = [];


    for(var m=0;m<methods_list.length;m++) {

        temp_array = [];

        for (var i = 0; i < question_list.length; i++) {

            temp = [];

            for (var j = 0; j < question_list[i].length; j++) {

                temp.push(Math.random());
            }

            temp_array.push(temp);

        }

        methods_value.push(temp_array);

    }


};


var display = function(){



    index_array = new Array(methods_list.length);
    for(var i=0;i<index_array.length;i++){

        index_array[i] = -1;

    }

    var initial_yes = true;

    for(var m=0;m<methods_list.length;m++){

        temp = document.getElementsByName(methods_list[m]);

        for(var i=0;i<temp.length;i++){

            if(temp[i].checked){

                if(initial_yes){

                    var initial_val = i;
                    initial_yes = false;
                    index_array[m] = i;
                    break;

                }else{
                    if(initial_val !==i){

                        alert("select same question");
                        return;

                    }else{
                        index_array[m] = i;
                        break;
                    }
                }
            }
        }
    }

    if(initial_yes){
        alert("select something!!");
        return;
    }

    var question_title = document.getElementById("question_title");
    var explanation_text = document.getElementById("explanation_about_questions");

    question_title.innerHTML = title_list[initial_val];

    console.log(title_list[initial_val]);

    explanation_text.innerHTML = explanations_list[initial_val];


    LegendOptions = [];

    for(var i=0;i<methods_list.length;i++){
        if(index_array[i] !== -1){
            LegendOptions.push(methods_list[i]);
        }
    }

    subject_index = question_list[index_array[0]];
    title = title_list[index_array[0]];
    chart_title = document.getElementById("chart_title");
    chart_title.innerHTML = title;

    var d = [];

    var n = 0;
    for(var m=0;m<methods_value.length;m++){
        if(index_array[m] !== -1){
            d.push([]);
            for(var j=0;j<methods_value[m][index_array[m]].length;j++){

                var temp = {};

                temp.axis = subject_index[j];
                temp.value = methods_value[m][index_array[m]][j];
                d[n].push(temp);

            }
            n += 1;
        }
    }


//Options for the Radar chart, other than default
    var mycfg = {
        w: w,
        h: h,
        maxValue: 0.6,
        levels: 6,
        ExtraWidthX: 300
    };


//Call function to draw the Radar chart
//Will expect that data is in %'s
    RadarChart.draw("#chart", d, mycfg);

////////////////////////////////////////////
/////////// Initiate legend ////////////////
////////////////////////////////////////////

    var svg = d3.select('#body')
        .selectAll('svg')
        .append('svg')
        .attr("width", w+300)
        .attr("height", h);




//Initiate Legend
    var legend = svg.append("g")
            .attr("class", "legend")
            .attr("height", 100)
            .attr("width", 300)
            .attr('transform', 'translate(90,20)')
            .attr("fill", "black")
        ;


//Create colour squares
    legend.selectAll('rect')
        .data(LegendOptions)
        .enter()
        .append("rect")
        .attr("x", w )
        .attr("y", function(d, i){ return i * 20 + 20;})
        .attr("width", 10)
        .attr("height", 10)
        .style("fill", function(d, i){ return colorscale(i);})
    ;


//Create text next to squares
    legend.selectAll('text')
        .data(LegendOptions)
        .enter()
        .append("text")
        .attr("x", w + 20)
        .attr("y", function(d, i){ return i * 20 + 29;})
        .attr("font-size", "15px")
        .attr("fill", "black")
        .text(function(d) { return d; })
    ;
}

