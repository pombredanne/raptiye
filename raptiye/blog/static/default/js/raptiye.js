 // raptiye
 // Copyright (C) 2009  Alper Kanat <alperkanat@raptiye.org>
 //
 // This program is free software: you can redistribute it and/or modify
 // it under the terms of the GNU General Public License as published by
 // the Free Software Foundation, either version 3 of the License, or
 // (at your option) any later version.
 //
 // This program is distributed in the hope that it will be useful,
 // but WITHOUT ANY WARRANTY; without even the implied warranty of
 // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 // GNU General Public License for more details.
 //
 // You should have received a copy of the GNU General Public License
 // along with this program. If not, see <http://www.gnu.org/licenses/>.

// --- EVENT HANDLERS START ---------------------------------------------------

$(document).on('click', '.timeline_row', function(e) {
    var year = $(this).find('.timeline_row_value a').text();

    if (! year) {
        return;
    }

    // first close any expanded year
    $('.timeline_sub_row:not(.month_' + year + ')').slideUp();

    // expand the clicked year
    $('.month_' + year).slideToggle();

    e.preventDefault();
});

$(document).on({
    focus: function(e) {
        $(this).addClass('extended');
    },
    blur: function(e) {
        $(this).removeClass('extended');
    }
}, '#search_container input');

// --- EVENT HANDLERS END -----------------------------------------------------

$(function() {
    $('.blog_entry_content a').attr('target', '_blank');
});