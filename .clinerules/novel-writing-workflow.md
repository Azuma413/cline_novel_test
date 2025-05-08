## Brief overview
This document outlines the rules and workflow for a novel writing project. It details the structure of setting files, the writing process in different modes, and guidelines for updating settings and project intelligence.

## Setting Structure
The setting for the novel is organized into five core files:
-   `StoryBrief.md`: Contains the summary of the story, its goals, and key elements to maintain consistency. This is the most crucial file for story coherence.
-   `Character.md`: Describes the characteristics of the story's characters. Character portrayals must align with these settings.
-   `OtherSetting.md`: Includes all non-character-related settings, such as place names, important plot points, and notes for future scenes.
-   `Sample.txt`: Provides a writing sample to be emulated for stylistic consistency. This sample is unrelated to the story's content.
-   `Outline.md`: Summarizes the plot of the story, with each chapter's content described in a few hundred characters. Completed chapters are linked to their respective file names. This file also indicates the next part to be written.

## Workflow

### Plan Mode
1.  **Read Setting Files**: Review all core setting files (`StoryBrief.md`, `Character.md`, `OtherSetting.md`, `Sample.txt`, `Outline.md`) to understand the story's overview and current writing status.
2.  **Determine Next Steps**: Identify the next content to be written based on the `Outline.md`.
3.  **Create Plan (if files incomplete)**: If setting files are incomplete or need updates, formulate a plan to address this.
4.  **Document Plan**: Communicate the plan in the chat.
5.  **Verify Context (if files complete)**: If setting files are complete, verify understanding of the context.
6.  **Develop Writing Strategy**: Formulate a strategy for the writing task.
7.  **Present Approach**: Present the writing approach for approval.

### Act Mode
1.  **Check Setting**: Before any writing, review all setting files.
2.  **Update Outline (if needed)**: If the next part to be written is not yet described in `Outline.md`, add a summary for it first.
3.  **Review Previous Chapter**: Check the content of the preceding chapter file (e.g., `X-1.txt` in the `MainStory` folder).
4.  **Write New Chapter**: Create the new chapter file (e.g., `X.txt`) in the `MainStory` folder.
    -   Target length: Approximately 2000 characters per chapter.
    -   Style: Write with detailed descriptions, especially for scenery and psychological states. Avoid overly poetic or exaggerated expressions.
5.  **Verify Consistency**: After writing, check the new chapter against the Setting files for any discrepancies.
6.  **Check Word Count**: Run `python counter.py` to ensure the written chapter meets the 2000-character minimum.
7.  **Update Setting (if applicable)**: If new settings were introduced or existing ones changed during writing, update the relevant Setting files.
8.  **Update .clinerules (if needed)**: If new patterns or preferences emerge, document them.
9.  **Document Changes**: Report the work done.

## Update Setting
The Setting files must be updated when:
1.  The user introduces new settings to the story.
2.  The story's settings or plot are changed.
3.  New settings or plot elements are added to the story.

The process for updating settings involves:
1.  Reviewing ALL setting files.
2.  Documenting the current state.
3.  Clarifying the next steps.
4.  Updating `.clinerules` if the update process reveals new project intelligence.

## Project Intelligence (.clinerules)
The `.clinerules` file serves as a learning journal for the project.
-   **Purpose**: To capture important patterns, user preferences, and project-specific intelligence to improve workflow efficiency.
-   **Content to Capture**:
    -   Critical implementation paths.
    -   User preferences and workflow.
    -   Project-specific patterns (e.g., writing style nuances, common plot devices).
    -   Known challenges (e.g., maintaining character voice, plot consistency).
    -   Evolution of project decisions.
    -   Tool usage patterns specific to the novel writing.
-   **Process**:
    1.  **Identify Pattern**: Recognize a new, recurring, or important aspect of the project or workflow.
    2.  **Validate with User**: Confirm the observation or preference.
    3.  **Document in .clinerules**: Add the insight to the relevant `.clinerules` file.
-   **Application**:
    1.  Read `.clinerules` at the start of a session or when undertaking a new task.
    2.  Apply learned patterns to the current work.
    3.  Continuously improve future work based on this documented intelligence.
