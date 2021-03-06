/*==========================================
  Green Bar
==========================================*/

addEvent(window, "load", init_tables);

function init_tables() {
    greenbar_init();
    bluebar_init();
}

function greenbar_init() {
    // Find all tables with class greenbar and make them greenbar
    if (!document.getElementsByTagName) return;
    tbls = document.getElementsByTagName("table");
    for (ti=0;ti<tbls.length;ti++) {
        if (hasClassName(tbls[ti], "greenbar")) makeGreenbar(tbls[ti]);
    }
}

function bluebar_init() {
    // Find all tables with class greenbar and make them greenbar
    if (!document.getElementsByTagName) return;
    tbls = document.getElementsByTagName("table");
    for (ti=0;ti<tbls.length;ti++) {
        if (hasClassName(tbls[ti], "bluebar")) makeBluebar(tbls[ti]);
    }
}

function makeGreenbar(table) {
    if (!table) return;
    var trs = table.tBodies[0].rows;
    for (var i = 0; i < trs.length; i++) removeClassName(trs[i], "even");
    for (var i = 0; i < trs.length; i += 2) {
        if(!hasClassName(trs[i], "sectionheader")) addClassName(trs[i], "even");
    };
}

function makeBluebar(table) {
    if (!table) return;
    var trs = table.tBodies[0].rows;
    for (var i = 0; i < trs.length; i++) removeClassName(trs[i], "even");
    for (var i = 0; i < trs.length; i += 2) {
        if(!hasClassName(trs[i], "sectionheader")) addClassName(trs[i], "even");
    };
}







