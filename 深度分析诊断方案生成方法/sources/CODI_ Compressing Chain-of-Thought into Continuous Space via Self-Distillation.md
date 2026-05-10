> Source: https://aclanthology.org/2025.emnlp-main.36/

CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation - ACL Anthology

[![ACL Logo](https://aclanthology.org/images/acl-logo.svg)
ACL Anthology](https://aclanthology.org/)


* [News(current)](/posts/)
* [FAQ(current)](/faq/)
* [Corrections(current)](/info/corrections/)
* [Submissions(current)](/info/contrib/)
* [GitHub](https://github.com/acl-org/acl-anthology/)

## [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36.pdf)

[Zhenyi Shen](/people/zhenyi-shen/unverified/),
[Hanqi Yan](/people/hanqi-yan/unverified/),
[Linhai Zhang](/people/linhai-zhang/unverified/),
[Zhanghao Hu](/people/zhanghao-hu/unverified/),
[Yali Du](/people/yali-du/),
[Yulan He](/people/yulan-he/)

##### Correct Metadata for

Use this form to create a GitHub issue with structured data describing the correction. You will need a GitHub account.
Once you create that issue, the correction will be reviewed by a staff member.

⚠️ Mobile Users: Submitting this form to create a new issue will only work with github.com, not the GitHub Mobile app.

**Important**: The Anthology treat PDFs as authoritative. Please use this form only to correct data
that is out of line with the PDF. See [our corrections
guidelines](https://aclanthology.org/info/corrections/) if you need to change the PDF.

Title
Adjust the title. Retain tags such as
<fixed-case>.

Authors
Adjust author names and order to match the
PDF.Add Author

Abstract
Correct abstract if needed. Retain XML formatting tags such as <tex-math>. You may use <b>...</b> for **bold**, <i>...</i> for *italic*, and <url>...</url> for URLs.

Verification against PDF
Ensure that the new title/authors match the snapshot below. (If there
is no snapshot or it is too small, consult [the PDF](#).)

[![]()](#)

Authors concatenated from the text boxes above:

ALL author names match the snapshot above—including
middle initials, hyphens, and accents.

Create GitHub issue for staff review

---

##### Abstract

Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by encouraging step-by-step reasoning in natural language. However, leveraging a latent continuous space for reasoning may offer benefits in terms of both efficiency and robustness. Prior implicit CoT methods attempt to bypass language completely by reasoning in continuous space but have consistently underperformed compared to the standard explicit CoT approach. We introduce CODI (Continuous Chain-of-Thought via Self-Distillation), a novel training framework that effectively compresses natural language CoT into continuous space. CODI jointly trains a teacher task (Explicit CoT) and a student task (Implicit CoT), distilling the reasoning ability from language into continuous space by aligning the hidden states of a designated token. Our experiments show that CODI is the first implicit CoT approach to match the performance of explicit CoT on GSM8k at the GPT-2 scale, achieving a 3.1x compression rate and outperforming the previous state-of-the-art by 28.2% in accuracy. CODI also demonstrates robustness, generalizable to complex datasets, and interpretability. These results validate that LLMs can reason effectively not only in natural language, but also in a latent continuous space. Code is available at https://github.com/zhenyi4/codi.

Anthology ID:
:   2025.emnlp-main.36

Volume:
:   [Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing](/volumes/2025.emnlp-main/)

Month:
:   November

Year:
:   2025

Address:
:   Suzhou, China

Editors:
:   [Christos Christodoulopoulos](/people/christos-christodoulopoulos/),
    [Tanmoy Chakraborty](/people/tanmoy-chakraborty/),
    [Carolyn Rose](/people/carolyn-rose/),
    [Violet Peng](/people/violet-peng/unverified/)

Venue:
:   [EMNLP](/venues/emnlp/ "Conference on Empirical Methods in Natural Language Processing")

SIG:


Publisher:
:   Association for Computational Linguistics

Note:


Pages:
:   677–693

Language:


URL:
:   <https://aclanthology.org/2025.emnlp-main.36/>

DOI:
:   [10.18653/v1/2025.emnlp-main.36](https://doi.org/10.18653/v1/2025.emnlp-main.36 "To the current version of the paper by DOI")

Bibkey:
:   shen-etal-2025-codi

Cite (ACL):
:   Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. 2025. [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36/). In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 677–693, Suzhou, China. Association for Computational Linguistics.

Cite (Informal):
:   [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36/) (Shen et al., EMNLP 2025)

Copy Citation:
:   BibTeX
    Markdown
    MODS XML
    Endnote
    More
    options…

PDF:
:   <https://aclanthology.org/2025.emnlp-main.36.pdf>

Checklist:
:   [2025.emnlp-main.36.checklist.pdf](https://aclanthology.org/attachments/2025.emnlp-main.36.checklist.pdf)

[PDF](https://aclanthology.org/2025.emnlp-main.36.pdf "Open PDF of 'CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation'")[Cite](# "Open dialog for exporting citations")[Search](https://www.semanticscholar.org/search?+q=CODI%3A+Compressing+Chain-of-Thought+into+Continuous+Space+via+Self-Distillation "Search for 'CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation' on Semantic Scholar")[Checklist](https://aclanthology.org/attachments/2025.emnlp-main.36.checklist.pdf "Open checklist for 'CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation'")[Fix data](# "Correct problems with title, author list, and abstract")

---

##### Export citation

* [BibTeX](#citeBibtex)
* [MODS XML](#citeMods)
* [Endnote](#citeEndnote)
* [Preformatted](#citeMarkdown)

```
@inproceedings{shen-etal-2025-codi,
    title = "{CODI}: Compressing Chain-of-Thought into Continuous Space via Self-Distillation",
    author = "Shen, Zhenyi  and
      Yan, Hanqi  and
      Zhang, Linhai  and
      Hu, Zhanghao  and
      Du, Yali  and
      He, Yulan",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.36/",
    doi = "10.18653/v1/2025.emnlp-main.36",
    pages = "677--693",
    ISBN = "979-8-89176-332-6",
    abstract = "Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by encouraging step-by-step reasoning in natural language. However, leveraging a latent continuous space for reasoning may offer benefits in terms of both efficiency and robustness. Prior implicit CoT methods attempt to bypass language completely by reasoning in continuous space but have consistently underperformed compared to the standard explicit CoT approach. We introduce CODI (Continuous Chain-of-Thought via Self-Distillation), a novel training framework that effectively compresses natural language CoT into continuous space. CODI jointly trains a teacher task (Explicit CoT) and a student task (Implicit CoT), distilling the reasoning ability from language into continuous space by aligning the hidden states of a designated token. Our experiments show that CODI is the first implicit CoT approach to match the performance of explicit CoT on GSM8k at the GPT-2 scale, achieving a 3.1x compression rate and outperforming the previous state-of-the-art by 28.2{\%} in accuracy. CODI also demonstrates robustness, generalizable to complex datasets, and interpretability. These results validate that LLMs can reason effectively not only in natural language, but also in a latent continuous space. Code is available at https://github.com/zhenyi4/codi."
}
```

Download as
File
Copy to Clipboard

```
<?xml version="1.0" encoding="UTF-8"?>
<modsCollection xmlns="http://www.loc.gov/mods/v3">
<mods ID="shen-etal-2025-codi">
    <titleInfo>
        <title>CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation</title>
    </titleInfo>
    <name type="personal">
        <namePart type="given">Zhenyi</namePart>
        <namePart type="family">Shen</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Hanqi</namePart>
        <namePart type="family">Yan</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Linhai</namePart>
        <namePart type="family">Zhang</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Zhanghao</namePart>
        <namePart type="family">Hu</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Yali</namePart>
        <namePart type="family">Du</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Yulan</namePart>
        <namePart type="family">He</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <originInfo>
        <dateIssued>2025-11</dateIssued>
    </originInfo>
    <typeOfResource>text</typeOfResource>
    <relatedItem type="host">
        <titleInfo>
            <title>Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing</title>
        </titleInfo>
        <name type="personal">
            <namePart type="given">Christos</namePart>
            <namePart type="family">Christodoulopoulos</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <name type="personal">
            <namePart type="given">Tanmoy</namePart>
            <namePart type="family">Chakraborty</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <name type="personal">
            <namePart type="given">Carolyn</namePart>
            <namePart type="family">Rose</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <name type="personal">
            <namePart type="given">Violet</namePart>
            <namePart type="family">Peng</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <originInfo>
            <publisher>Association for Computational Linguistics</publisher>
            <place>
                <placeTerm type="text">Suzhou, China</placeTerm>
            </place>
        </originInfo>
        <genre authority="marcgt">conference publication</genre>
        <identifier type="isbn">979-8-89176-332-6</identifier>
    </relatedItem>
    <abstract>Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by encouraging step-by-step reasoning in natural language. However, leveraging a latent continuous space for reasoning may offer benefits in terms of both efficiency and robustness. Prior implicit CoT methods attempt to bypass language completely by reasoning in continuous space but have consistently underperformed compared to the standard explicit CoT approach. We introduce CODI (Continuous Chain-of-Thought via Self-Distillation), a novel training framework that effectively compresses natural language CoT into continuous space. CODI jointly trains a teacher task (Explicit CoT) and a student task (Implicit CoT), distilling the reasoning ability from language into continuous space by aligning the hidden states of a designated token. Our experiments show that CODI is the first implicit CoT approach to match the performance of explicit CoT on GSM8k at the GPT-2 scale, achieving a 3.1x compression rate and outperforming the previous state-of-the-art by 28.2% in accuracy. CODI also demonstrates robustness, generalizable to complex datasets, and interpretability. These results validate that LLMs can reason effectively not only in natural language, but also in a latent continuous space. Code is available at https://github.com/zhenyi4/codi.</abstract>
    <identifier type="citekey">shen-etal-2025-codi</identifier>
    <identifier type="doi">10.18653/v1/2025.emnlp-main.36</identifier>
    <location>
        <url>https://aclanthology.org/2025.emnlp-main.36/</url>
    </location>
    <part>
        <date>2025-11</date>
        <extent unit="page">
            <start>677</start>
            <end>693</end>
        </extent>
    </part>
</mods>
</modsCollection>
```

Download as
File
Copy to Clipboard

```
%0 Conference Proceedings
%T CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation
%A Shen, Zhenyi
%A Yan, Hanqi
%A Zhang, Linhai
%A Hu, Zhanghao
%A Du, Yali
%A He, Yulan
%Y Christodoulopoulos, Christos
%Y Chakraborty, Tanmoy
%Y Rose, Carolyn
%Y Peng, Violet
%S Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing
%D 2025
%8 November
%I Association for Computational Linguistics
%C Suzhou, China
%@ 979-8-89176-332-6
%F shen-etal-2025-codi
%X Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by encouraging step-by-step reasoning in natural language. However, leveraging a latent continuous space for reasoning may offer benefits in terms of both efficiency and robustness. Prior implicit CoT methods attempt to bypass language completely by reasoning in continuous space but have consistently underperformed compared to the standard explicit CoT approach. We introduce CODI (Continuous Chain-of-Thought via Self-Distillation), a novel training framework that effectively compresses natural language CoT into continuous space. CODI jointly trains a teacher task (Explicit CoT) and a student task (Implicit CoT), distilling the reasoning ability from language into continuous space by aligning the hidden states of a designated token. Our experiments show that CODI is the first implicit CoT approach to match the performance of explicit CoT on GSM8k at the GPT-2 scale, achieving a 3.1x compression rate and outperforming the previous state-of-the-art by 28.2% in accuracy. CODI also demonstrates robustness, generalizable to complex datasets, and interpretability. These results validate that LLMs can reason effectively not only in natural language, but also in a latent continuous space. Code is available at https://github.com/zhenyi4/codi.
%R 10.18653/v1/2025.emnlp-main.36
%U https://aclanthology.org/2025.emnlp-main.36/
%U https://doi.org/10.18653/v1/2025.emnlp-main.36
%P 677-693
```

Download as
File
Copy to Clipboard

##### Markdown (Informal)

[CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36/) (Shen et al., EMNLP 2025)

* [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36/) (Shen et al., EMNLP 2025)

##### ACL

* Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. 2025. [CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.36/). In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 677–693, Suzhou, China. Association for Computational Linguistics.

Copy Markdown to
Clipboard
Copy ACL to
Clipboard

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
ACL materials are Copyright © 1963–2026 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License](https://creativecommons.org/licenses/by-nc-sa/3.0/). Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

The ACL Anthology is managed and built by the [ACL Anthology team](/info/credits/) of volunteers.

*Site last built on 08 May 2026 at 14:01 UTC with [commit ff75cc6](https://github.com/acl-org/acl-anthology/tree/ff75cc647f6edb04c49a776ce3f014b325a91920).*