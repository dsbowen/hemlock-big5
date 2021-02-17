<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style>##hemlock_big5.**big5**

<p class="func-header">
    <i>def</i> hemlock_big5.<b>big5</b>(<i>*items, version='IPIP-50', page=False, require=False, choice_labels=5, include_instructions=True, shuffle_items=False, record_index=False</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-big5/blob/master/hemlock_big5/__init__.py#L53">[source]</a>
</p>

Create a big 5 personality questionnaire.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>*items : <i></i></b>
<p class="attr">
    Names of big 5 items to include. If no items are specified, this function returns all big 5 items in the specified version.
</p>
<b>version : <i>str, default='IPIP-50'</i></b>
<p class="attr">
    Version of the big 5 questionnaire. Currently supported are <code>'IPIP-50'</code> (50-item version from the Interntaional Personality Item Pool), <code>'TIPI'</code> (Ten-Item Personality Inventory), and <code>'BFI-10'</code> (10-item Big 5 Inventory).
</p>
<b>page : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that this function should return a page with the big 5 items. Otherwise, return a list of questions.
</p>
<b>require : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that responses are required (for all items).
</p>
<b>choice_labels : <i>int or list, default=5</i></b>
<p class="attr">
    List of strings for the choice labels participants can select. May also be <code>5</code> or <code>7</code> for 5 or 7 default labels.
</p>
<b>include_instructions : <i>bool, default=True</i></b>
<p class="attr">
    Indicates that an instructions label should be included before the items.
</p>
<b>shuffle_items : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that items should be shuffled.
</p>
<b>record_index : <i>bool, default=False</i></b>
<p class="attr">
    Indicates to record the index of the big 5 items as they appear on the page. Only applies of <code>page</code> is <code>True</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>big5_questionnaire : <i>hemlock.Page or list of hemlock.Question</i></b>
<p class="attr">
    If <code>page</code> is <code>True</code>, this function returns a page containing the requested big 5 items. Otherise, it returns a list of questions.
</p></td>
</tr>
    </tbody>
</table>



##hemlock_big5.**big5_traits**

<p class="func-header">
    <i>def</i> hemlock_big5.<b>big5_traits</b>(<i>*traits, version='IPIP-50', **kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-big5/blob/master/hemlock_big5/__init__.py#L162">[source]</a>
</p>

Create a big 5 personality questionnaire for specified personality traits.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>*traits : <i></i></b>
<p class="attr">
    Strings of requested traits, <code>'E'</code> for extraversion, <code>'A'</code> for agreeableness, <code>'C'</code> for conscientiousness, <code>'N'</code> for neuroticism, <code>'O'</code> for openness.
</p>
<b>version : <i>str, default='IPIP-50'</i></b>
<p class="attr">
    Version of the big 5 questionnaire.
</p>
<b>**kwargs : <i></i></b>
<p class="attr">
    Keyword arguments are passed to <code>big5</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>big5_questionnaire : <i>hemlock.Page or list of hemlock.Question</i></b>
<p class="attr">
    If <code>page</code> is <code>True</code>, this function returns a page containing the requested big 5 items. Otherise, it returns a list of questions.
</p></td>
</tr>
    </tbody>
</table>

