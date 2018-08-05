$(document).ready(function() {
    $('#team_engine').on('submit', function(event){
        $.ajax({
            data : {
                team_query: $('#team_query').val()
            },
            type: 'POST',
            url: '/'
        })
        .done(function(data) {
            document.getElementById('team_search').innerHTML = '';
            // alert(data['data'][0]['score'])

            for (var i = 0; i < data['data'].length; i++) {
                entry = data['data'][i];

                row = ''
                row += '<tr>'
                row += '<td>' + entry['link'] + '</td>'
                row += '<td>' + entry['team'] + '</td>'
                row += '<td>' + entry['score'] + '</td>'
                row += '</tr>'

                document.getElementById('team_search').innerHTML += row;
            }

        });
        event.preventDefault();
    });
});
