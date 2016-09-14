from reports.forms import DriveForm


def add_drive(final_drive):
    initial_data = dict()

    initial_data['student'] = final_drive.student_id
    initial_data['instructor'] = final_drive.instructor_id
    initial_data['date'] = final_drive.final_drive_date
    initial_data['date'] = final_drive.final_drive_date
    initial_data['score'] = final_drive.final_drive_total_score
    initial_data['deductions'] = final_drive.final_drive_total_deductions
    initial_data['comments'] = final_drive.final_drive_comments
    initial_data['hours_driven'] = final_drive.final_drive_hours_driven
    initial_data['hours_observed'] = final_drive.final_drive_hours_observed
    initial_data['updated'] = final_drive.last_updated

    form = DriveForm(data=initial_data)

    if form.is_valid():
        form.save()


    return "Done."