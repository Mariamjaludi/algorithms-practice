# frozen_string_literal: true

class Person
  def initialize(firstName, lastName, id)
    @firstName = firstName
    @lastName = lastName
    @id = id
  end

  def printPerson
    print('Name: ', @lastName, ', ' + @firstName, "\nID: ", @id)
  end
end

class Student < Person
  def initialize(firstName, lastName, id, scores)
    super(firstName, lastName, id)
    @scores = scores
  end

  def calculate
    grade = @scores.sum / @scores.length
    case grade
    when 90..100
      'O'
    when 80..89
      'E'
    when 70..79
      'A'
    when 55..69
      'P'
    when 40..54
      'D'
    when proc { |n| n < 40 }
      'T'
    end
  end
end
