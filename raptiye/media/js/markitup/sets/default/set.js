// ----------------------------------------------------------------------------
// markItUp!
// ----------------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// ----------------------------------------------------------------------------
// Html tags
// http://en.wikipedia.org/wiki/html
// ----------------------------------------------------------------------------
// Basic set. Feel free to add more tags
// ----------------------------------------------------------------------------
mySettings = {
    nameSpace: 'html',
    resizeHandle: true,
    previewAutoRefresh: true,
    previewTemplatePath: '/blog/show_preview/',
    previewInWindow: 'width=1024, height=600, resizable=yes, scrollbars=yes, location=no',
    onShiftEnter: {keepDefault: false, replaceWith: '<br />\n'},
    onCtrlEnter: {keepDefault: false, openWith: '\n<p>', closeWith: '</p>'},
    onTab: {keepDefault: false, replaceWith: '    '},
    markupSet: [
        {name: 'Heading 1', key: '1', openWith: '<h1(!( class="[![Class]!]")!)>', closeWith: '</h1>', placeHolder: 'Your title here...'},
        {name: 'Heading 2', key: '2', openWith: '<h2(!( class="[![Class]!]")!)>', closeWith: '</h2>', placeHolder: 'Your title here...'},
        {name: 'Heading 3', key: '3', openWith: '<h3(!( class="[![Class]!]")!)>', closeWith: '</h3>', placeHolder: 'Your title here...'},
        {name: 'Heading 4', key: '4', openWith: '<h4(!( class="[![Class]!]")!)>', closeWith: '</h4>', placeHolder: 'Your title here...'},
        {name: 'Heading 5', key: '5', openWith: '<h5(!( class="[![Class]!]")!)>', closeWith: '</h5>', placeHolder: 'Your title here...'},
        {name: 'Heading 6', key: '6', openWith: '<h6(!( class="[![Class]!]")!)>', closeWith: '</h6>', placeHolder: 'Your title here...'},
        {name: 'Paragraph', openWith: '<p(!( class="[![Class]!]")!)>', closeWith: '</p>'},
        {name: 'Div Container', openWith: '<div(!( class="[![Class]!]")!)>', closeWith: '</div>', placeHolder: 'Your content here...'},
        {name: 'Blockquote', openWith: '<blockquote(!( class="[![Class]!]")!)>', closeWith: '</blockquote>', placeHolder: 'Your content here...'},
        {separator: '---------------'},
        {name: 'Bold', key: 'B', openWith: '<strong>', closeWith: '</strong>'},
        {name: 'Italic', key: 'I', openWith: '<em>', closeWith: '</em>'},
        {name: 'Stroke through', key: 'S', openWith: '<del>', closeWith: '</del>'},
        {separator:'---------------'},
        {name: 'Ul', openWith: '<ul>\n', closeWith: '</ul>\n'},
        {name: 'Ol', openWith: '<ol>\n', closeWith: '</ol>\n'},
        {name: 'Li', openWith: '<li>', closeWith: '</li>'},
        {separator: '---------------'},
        {name: 'Picture', key: 'P', replaceWith: '<img src="[![Source:!:http://]!]" alt="[![Alternative text]!]" />'},
        {
            name: 'Link',
            key: 'L',
            openWith: '<a href="[![Link:!:http://]!]"(!( title="[![Title]!]")!)>',
            closeWith: '</a>',
            placeHolder: 'Your text to link...'
        },
        {separator: '---------------'},
        {
            name: 'Clean',
            replaceWith: function(h) {
                return h.selection.replace(/<(.*?)>/g, "")
            }
        },
        {name: 'Preview', call:'preview', className:'preview' }
    ]
}