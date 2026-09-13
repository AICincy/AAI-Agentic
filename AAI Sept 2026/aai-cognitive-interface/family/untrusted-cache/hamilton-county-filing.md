# Hamilton County Filing Integration

## Source Authority

This reference is a workflow aid derived from Hamilton County court and clerk
materials. Before a filing-ready deliverable, verify the current local-rules
version and every dispositive filing requirement against the official court
or clerk source. Do not treat a bundled revision date as proof of current law.

The current official local-rules page was verified on August 8, 2026 as
listing "Local Rules Book Version - Effective 4-24-26." Re-check it at each
filing because local rules can change.

Key source set:

1. Hamilton County Rules of Practice of the Court of Common Pleas,
   current official local-rules book, including the rules governing
   pleadings, motion practice, and electronic filing as applicable.

2. Hamilton County Clerk of Courts, "Helpful Hints: How to Do Things
   for E-Filing Users" (Revision 7-1-19).

3. Hamilton County Clerk of Courts, "Guide to Electronic Filing"
   (Revision 5.1, 7-1-19).

## Applicability

Identify the exact court, division, and case type before applying any local
rule in this reference. The Hamilton County Court of Common Pleas local-rules
book applies to its General Division. Do not apply that book by default to a
different Hamilton County court or division.

Route local-rule verification as follows:

| Target | Controlling local source to verify fresh |
|---|---|
| Common Pleas General Division civil or criminal | Common Pleas General Division local-rules book |
| Domestic Relations | Domestic Relations Court's own current rules |
| Court of Appeals | First District Court of Appeals' own current rules |
| Municipal Court | Hamilton County Municipal Court and applicable clerk procedures |
| Probate or Juvenile | That division's own current rules |

Clerk procedures in this reference apply only when the current official clerk
source confirms they cover the identified court, case type, filing channel,
and document purpose.

IF the case is in a different Ohio county or a different state:
THEN do not apply these rules. Apply the rules of that jurisdiction
instead. Generic Ohio procedural rules (Ohio Rules of Civil Procedure,
Ohio Rules of Criminal Procedure, Rules of Superintendence) apply
statewide and are separate from this reference.

## Filing Format Requirements

The Local Rule 34 requirements in this section are Common Pleas General
Division requirements. For another Hamilton County court or division,
determine the permitted and required format from that court's current rules
before producing filing output.

### Output format by document purpose

| Purpose | Required format | Authority |
|---|---|---|
| All filings (complaints, motions, memoranda, affidavits, analyses) | PDF or PDF/A | Local Rule 34(B)(7)(a) |
| Proposed Entries and Proposed Orders submitted to a judge | Microsoft Word (.doc or .docx) | Local Rule 34(B)(7)(b) |
| All other filings | PDF | Default |

Do not produce a docx file for a document that the clerk will receive
as a filing. The clerk will reject non-PDF filings (except proposed
entries/orders). Do not produce a PDF for a proposed entry or order
that a judge must sign. The judge needs an editable Word document.

### Page format

All documents must be on 8.5 x 11-inch paper. This matches the skill's
existing US Letter specification (12240 x 15840 DXA).

### File size

Maximum 20MB per document upload. If a document exceeds 20MB, split it
into parts. Each part must have its own cover page with the case caption,
case number, judge, and document title. The title on each part must be
keyed into the Document Caption box so the parts are tied together on
the docket.

For Common Pleas motions, each split part must use the filing type
"Motion" so copies are made for the judge's mailbox.

Example split naming:
  Part 1: "Motion to Suppress, Part 1 of 2, with Exhibits A through F"
  Part 2: "Motion to Suppress, Part 2 of 2, with Exhibits G through K"

### Electronic signature

Documents may be signed using /s/ followed by the filer's first, middle
(optional), and last name, typed on the signature line above the
standard identifying information. The /s/ alone is not sufficient. The
name must appear on the same line. The skill's attestation blocks
already include a signature line. When producing the final PDF, the
/s/ signature should appear above the underscore line.

Suggestion from the Clerk: use a bolded font larger than the document
body for the /s/ signature line.

## Pro Se E-Filing

This section describes Common Pleas General Division "A" case procedures.
Do not transfer them to another court or case type without current official
support.

### Exemption from mandatory e-filing

Local Rule 11(A) and Local Rule 34(A)(1) state that all "A" case filings
SHALL be filed electronically "unless the party is proceeding pro se."
Pro se filers are exempt from the mandatory e-filing requirement but may
e-file voluntarily.

### Pro se account differences

Pro se filers use their email address as the e-filing user ID (not an
Ohio Bar number). The account type is "Pro Se / Individual / Non-Attorney."
Copy costs for pro se filers are charged when the e-filing is processed,
not drawn from a pre-funded copy cost account.

### Credit card requirement

E-filing requires a valid American Express, Discover, MasterCard, or Visa
credit card. If the filing is rejected, the card is not charged.

## Motion Practice (Local Rule 14)

This section describes Common Pleas General Division motion practice. Do not
apply Local Rule 14 to another Hamilton County court or division without
verifying that court's own current motion rules.

### Memorandum requirement

Local Rule 14(A): "All motions shall be accompanied by a memorandum in
support of the motion which shall be a brief statement of the grounds
for the same, with citations of authorities relied upon, and (except in
the case of an ex parte motion) proof of service in accordance with
Civil Rule 5. All memorandum filed with a motion or in response thereto
shall include page and document references for all factual assertions."

This rule has two implications for this skill:

1. If the skill produces a suppression memo appendix, that appendix is
   NOT the memorandum required by Rule 14(A). The appendix is a factual
   attachment. A separate memorandum stating the legal grounds, citing
   authorities, and including page/document references must accompany
   the motion. The skill must flag this as a required companion document.

2. The Rule 14(A) requirement for "page and document references for all
   factual assertions" reinforces the skill's existing requirement that
   every finding cite exhibits. In Common Pleas General Division when the
   current rule applies, this is a local rule mandate rather than only best
   practice.

### Response timeline

Memorandum contra: 14 days from service of the motion.
Memorandum contra to summary judgment: 28 days from service.
Reply memorandum: 7 days from service of memorandum contra.
These periods may be extended for good cause.

### Oral argument

No motions in civil cases will be set for oral argument unless a written
request is made or the court directs it. If oral argument is desired,
note this conspicuously in the filing.

## Service Requirements

### Common Pleas Civil (existing cases)

Service is NOT automatically done by the e-filing system. The filer must
make service on all parties per Civil Rule 5. For clerk-assisted service,
file a separate Written Request for Service form. Do not append the
document to be served to the service request.

Service types and costs (per service):
  Certified mail (WRS): $9.00
  Registered international mail (WRSR): $9.00
  Express mail (WRSE): $27.00
  Foreign sheriff (WRSF): $30.00
  Ordinary mail (WRSO): no charge
  Process server (WRSP): no charge
  Sheriff (WRSS): $5.00

### Common Pleas Criminal

All motions and filings on criminal cases are served to the Prosecutor's
Office by the Clerk automatically. This is the only instance where
service is done without a written request form.

### Municipal Civil (existing cases)

All filings requiring service must include a Municipal Civil Service
Notification Form as the last page of the document. The filer must also
select service type(s) during the e-filing process.

This means: if the skill produces a document for filing in Municipal
Civil Court and the filer wants clerk-assisted service, the Service
Notification Form must be appended as the final page of the PDF before
upload. The skill flags this as a post-production step.

## Rejected Filing Consequences

Effective May 2, 2016, the Local Rules no longer allow a rejected filing
to be corrected and resubmitted to retain the original filing date. A
corrective filing receives a new confirmation number and a new file date.

This makes first-submission accuracy critical. Run the full validation
checklist before delivery. Verify that the filing type selection, page
count, document format, and service selections are correct before the
filer submits.

## AI-Assisted Court Submissions: Common Pleas General Division

Hamilton County Common Pleas Local Rule 49, "Use of Artificial Intelligence
in Court Submissions," appears in the official local-rules book effective
April 24, 2026. The rule covers AI assistance in creation or editing of a
document or evidence submitted to the court, including document generation,
evidence creation or analysis, and legal research. It requires disclosure at
submission through a certification attached to the document or evidence. The
certification identifies the type of AI used and certifies final review and
approval of the AI-assisted material.

For any AI-assisted filing to the General Division, verify the current Rule 49
text and applicability during the filing session, then include the required
disclosure/certification. Do not assume this Common Pleas General Division
rule governs a different Hamilton County court or division without checking
that court's current rules.

## Case Number Formats

| Court | Format | Example |
|---|---|---|
| Common Pleas Civil | [Court letter] [2-digit year] [5-digit number] | A 24 01234 |
| Common Pleas Criminal | B [2-digit year] [5-digit number] [-defendant letter] | B 24 01234-C |
| Court of Appeals | C [2-digit year] [5-digit number] | C 24 01234 |
| Domestic Relations | DR [2-digit year] [5-digit number] | DR 24 01234 |
| Municipal Civil | [2-digit year] CV [5-digit number] | 24 CV 01234 |

## Personal Identifier Requirements

Use the current Ohio Rules of Superintendence for personal identifiers and
filing privacy. The rules were restructured effective July 1, 2026. As of
August 8, 2026, Sup.R. 11.09 contains the relevant definitions and Sup.R.
11.13 governs omission of personal identifiers from case documents. Verify
the current numbering before filing. The responsibility for redaction rests
with the filer; do not assume the Clerk or Court will cure a disclosure.

When personal identifiers are necessary to the filing, they must be
submitted separately on a Personal Identifier Reference List form
provided by the Clerk.

If a date of birth must be referenced, use only the year. If an account
number must be referenced, use only the last four digits. If names of
minor children must be referenced, use initials or "CV" for "child victim."

## Documents Not Accepted for E-Filing

Civil Protection Orders, Notary Public Commissions, and Notary Public
Verifications must be filed in person. These cannot be e-filed.

A complete case dismissal cannot be e-filed if costs are owed on the case.
A partial dismissal may be e-filed but must be clearly labeled as partial
and must state that the case remains open.

## Sealed Cases and Sealed Documents

Filings may be made on sealed cases. The document must be clearly marked
below its title that the case is sealed. A copy of the filed document
will be given to the case judge.

A single document may be filed under seal if a court order on the case
docket authorizes sealing. The filer must note on the document the
order date authorizing the seal (e.g., "Document filed under seal
pursuant to Court Order of mm/dd/yyyy").

## Clerk Contact

E-Filing Coordinator: (513) 946-5612
Email: efilingclerk@cms.hamilton-co.org
Hours: 8:00 AM to 4:00 PM EST, Monday through Friday
In-person: Hamilton County Courthouse, Room 315 Issue Desk,
1000 Main Street, Cincinnati, OH 45202
