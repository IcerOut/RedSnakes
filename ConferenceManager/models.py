from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    conference = models.ForeignKey('Conference', on_delete=models.PROTECT)
    section = models.ForeignKey('Section', on_delete=models.PROTECT)

class PCMember(Author):
    pass

class PCCoChair(PCMember):
    pass

class Conference(models.Model):
    name = models.CharField(max_length=200)
    abstractSubmissionDeadline = models.DateField()
    paperSubmissionDeadline = models.DateField()
    startDate = models.DateField()
    endDate = models.DateField()
    resultsDeadline = models.DateField()
    scMember = models.ForeignKey('SCMember', on_delete=models.PROTECT)


    def assignPaperToReview(self):
        pass

    def assignSessionChair(self):
        pass

EVAL_DEC = [
    ("AC", "Accepted"),
    ("NE", "Not evaluate"),
    ("RE", "Rejected")
]

PAPER_KIND = [
    ("PDF", "pdf"),
    ("DOCX", "docx"),
    ("TXT", "text")
]

class Paper(models.Model):
    name = models.CharField(max_length=200)
    noPages = models.IntegerField()
    paperKind = models.CharField(max_length=3, choices=PAPER_KIND)
    evalDecision = models.CharField(max_length=2, choices=EVAL_DEC)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT)
    author = models.ManyToManyField(Author)


class PCMemberPaper(models.Model):
    pcMember = models.ForeignKey(PCMember, on_delete=models.PROTECT)
    paper = models.ForeignKey(Paper, on_delete=models.PROTECT)

EV_RESULT = [
    ("SA", "Strong accept"),
    ("WA", "Weak accept"),
    ("NE", "Neutral"),
    ("SR", "Strong reject"),
    ("WR", "Weak reject")
]

class EvaluationResult(models.Model):
    rezEv = models.CharField(max_length=2, choices=EV_RESULT)
    evaluationDate = models.DateField()
    pcMemberPaper = models.ForeignKey(PCMemberPaper, on_delete=models.PROTECT)


class BiddingResult(models.Model):
    resBid = models.CharField(max_length=200)
    biddingDate = models.DateField()
    pcMemberPaper = models.ForeignKey(PCMemberPaper, on_delete=models.PROTECT)


class Abstract(models.Model):
    keyWords = models.CharField(max_length=200)
    text = models.TextField()


class SCMember(models.Model):
    name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)


class Section(models.Model):
    name = models.CharField(max_length=200)
    scMember = models.OneToOneField(SCMember, on_delete=models.PROTECT, blank=True, null=True)
    # pcMember = models.OneToOneField(PCMember, on_delete=models.PROTECT, blank=True, null=True)
    paper = models.ForeignKey(Paper, on_delete=models.PROTECT)