var phenology = {};

phenology.initialize_phenology = function() {
    $('.dropdown a[data-toggle]').click(function() {
        var location = $(this).attr('href');
        window.location.href = location;
        return false;
    });
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
