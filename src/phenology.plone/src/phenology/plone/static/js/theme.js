var phenology = {};

phenology.initialize_phenology = function() {
    //~ phenology.initialize_sections();
}

phenology.equalHeight = function(group) {
    var tallest = 0;
    group.each(function() {
        var thisHeight = $(this).height();
        if(thisHeight > tallest) {
            tallest = thisHeight;
        }
    });
    group.height(tallest);
};

jQuery(phenology.initialize_phenology);
