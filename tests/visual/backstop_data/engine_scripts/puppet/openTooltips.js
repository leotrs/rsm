module.exports = async (page, scenario, vp) => {
    console.log('SCENARIO > ' + scenario.label);
    await require('./clickAndHoverHelper')(page, scenario);

    $("a.reference").tooltipster("open", () => {console.log("tooltip open")});
};
