<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script>
        function selectOnlyThis(id) {
            for (var i = 1;i <= 4; i++)
            {
                document.getElementById("Check" + i).checked = false;
            }
            document.getElementById(id).checked = true;
        }
    </script>
</head>
<body>
<form method="POST" action="/submit_survey">

  <fieldset class="form-group">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">How was your experience staying with us?</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            Excellent
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio1" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Very Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio1" id="gridRadios3" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio1" id="gridRadios4" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worse
          </label>
        </div>
              <div class="form-check">
          <input class="form-check-input" type="radio" name="radio1" id="gridRadios5" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worst
          </label>
        </div>
      </div>
    </div>
  </fieldset>


    <fieldset class="form-group">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">How was your experience staying with us?</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio2" id="gridRadios1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            Excellent
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio2" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Very Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio2" id="gridRadios3" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio2" id="gridRadios4" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worse
          </label>
        </div>
              <div class="form-check">
          <input class="form-check-input" type="radio" name="radio2" id="gridRadios5" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worst
          </label>
        </div>
      </div>
    </div>
  </fieldset>



      <fieldset class="form-group">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">How was your experience staying with us?</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio3" id="gridRadios1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            Excellent
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio3" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Very Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio3" id="gridRadios3" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio3" id="gridRadios4" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worse
          </label>
        </div>
              <div class="form-check">
          <input class="form-check-input" type="radio" name="radio3" id="gridRadios5" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worst
          </label>
        </div>
      </div>
    </div>
  </fieldset>



      <fieldset class="form-group">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">How was your experience staying with us?</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio4" id="gridRadios1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            Excellent
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio4" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Very Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio4" id="gridRadios3" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio4" id="gridRadios4" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worse
          </label>
        </div>
              <div class="form-check">
          <input class="form-check-input" type="radio" name="radio4" id="gridRadios5" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worst
          </label>
        </div>
      </div>
    </div>
  </fieldset>



      <fieldset class="form-group">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">How was your experience staying with us?</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio5" id="gridRadios1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            Excellent
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio5" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Very Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio5" id="gridRadios3" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Good
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radio5" id="gridRadios4" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worse
          </label>
        </div>
              <div class="form-check">
          <input class="form-check-input" type="radio" name="radio5" id="gridRadios5" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Worst
          </label>
        </div>
      </div>
    </div>
  </fieldset>










  <div class="form-group row">
    <div class="col-sm-2">Which butler served you the best?</div>
    <div class="col-sm-10">
      <div class="form-check">
        <input type="checkbox" id="Check1" value="Value1" onclick="selectOnlyThis(this.id)" name="check_answer" />
        <label class="form-check-label" for="gridCheck1">
          Butler 1
        </label><br>
        <input type="checkbox" id="Check2" value="Value1" onclick="selectOnlyThis(this.id)" name="check_answer" />
        <label class="form-check-label" for="gridCheck1">
          Butler 2
        </label><br>
        <input type="checkbox" id="Check3" value="Value1" onclick="selectOnlyThis(this.id)" name="check_answer" />
        <label class="form-check-label" for="gridCheck1">
          Butler 3
        </label><br>
                <input type="checkbox" id="Check4" value="Value1" onclick="selectOnlyThis(this.id)" name="check_answer"/>
        <label class="form-check-label" for="gridCheck1">
          Butler 4
        </label><br>
      </div>
    </div>
  </div>




    <div class="form-group row">
    <label for="inputEmail3" class="col-sm-2 col-form-label">What part of the butler's service did you like the most?</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputEmail3" placeholder="Answer" name="subjective1">
    </div>
  </div>
    <div class="form-group row">
    <label for="inputEmail3" class="col-sm-2 col-form-label">How can we improve your next visit?</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputEmail4" placeholder="Answer" name="subjective2">
    </div>
  </div>





  <div class="form-group row">
    <div class="col-sm-10">
      <input type="submit" class="btn btn-primary" name="submit_survey" value="Submit Survey">
    </div>
  </div>

</form>
</body>
</html>